import asyncio

from pyrogram import filters
from pyrogram.errors import MessageDeleteForbidden

from config import SUDO_USERS

data = {}


async def task(msg, warn=False, sec=None):
    if warn:
        user = msg.from_user or msg.sender_chat
        ids = await msg.reply_text(
            f"Sorry {user.mention if msg.from_user else msg.sender_chat.title} [<code>{user.id}</code>], you must wait for {sec}s before using this Command again.."
        )
        try:
            await asyncio.sleep(10)
            await ids.delete()
        except MessageDeleteForbidden:
            pass
        await asyncio.sleep(sec)
        gc = await ids.edit_text(
            f"Alright {user.mention if msg.from_user else msg.sender_chat.title} [<code>{user.id}</code>], your cooldown is over you can command again."
        )
        await asyncio.sleep(5)
        await gc.delete()


def wait(sec):
    async def ___(flt, _, msg):
        user_id = msg.from_user.id if msg.from_user else msg.sender_chat.id
        if user_id in SUDO_USERS:
            return True
        if user_id in data:
            if msg.date.timestamp() >= data[user_id]["timestamp"] + flt.data:
                data[user_id] = {"timestamp": msg.date.timestamp(), "warned": False}
                return True
            else:
                if not data[user_id]["warned"]:
                    data[user_id]["warned"] = True
                    asyncio.ensure_future(
                        task(msg, True, flt.data)
                    )  # for super accuracy use (future - time.time())
                    return False  # cause we dont need delete again

                asyncio.ensure_future(task(msg))
                return False
        else:
            data.update({user_id: {"timestamp": msg.date.timestamp(), "warned": False}})
            return True

    return filters.create(___, data=sec)
