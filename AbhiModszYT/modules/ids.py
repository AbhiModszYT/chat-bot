from pyrogram import filters
from pyrogram.enums import ParseMode

from AbhiModszYT import dev


@dev.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝘿 :]({message.link})** `{message_id}`\n"
    text += f"**[𝙔𝙤𝙪𝙧 𝙄𝘿 :](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[𝙐𝙨𝙚𝙧 𝙄𝘿 :](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧 𝘿𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩.", quote=True)

    text += f"**[𝙂𝙧𝙤𝙪𝙥/𝘾𝙝𝙖𝙩 𝙄𝙙 :](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[𝙍𝙚𝙥𝙡𝙮 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝘿 :]({reply.link})** `{reply.id}`\n"
        text += f"**[𝙍𝙚𝙥𝙡𝙮 𝙐𝙨𝙚𝙧 𝙄𝘿 :](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
