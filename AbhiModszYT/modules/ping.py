# Don't remove This Line From Here. Tg: AM_YTBott
# Github :- AbhiModszYT

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from AbhiModszYT import BOT_NAME, dev
from AbhiModszYT.database.chats import add_served_chat
from AbhiModszYT.database.users import add_served_user
from AbhiModszYT.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="𝙋𝙞𝙣𝙜 𝙋𝙤𝙣𝙜...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"𝙃𝙚𝙮 𝘽𝙪𝙙𝙙𝙮!!\n{BOT_NAME} 𝙄𝙨 𝘼𝙡𝙞𝙫𝙚 𝘼𝙣𝙙 𝙒𝙤𝙧𝙠𝙞𝙣𝙜 𝙁𝙞𝙣𝙚 𝙒𝙞𝙩𝙝 𝙋𝙞𝙣𝙜 𝙊𝙛 \n➥ `{ms}` ms\n\n<b>|| 𝙈𝙖𝙙𝙚 ✨ 𝘽𝙮 [𝘿𝙚𝙫𝙡𝙤𝙫𝙚𝙥𝙚𝙧](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
