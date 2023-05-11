from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from AbhiModszYT import BOT_USERNAME, OWNER

DEV_OP = [
    [
        InlineKeyboardButton(text="👑 𝗢𝘄𝗻𝗲𝗿", user_id=OWNER),
        InlineKeyboardButton(text="💫 𝘾𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙂𝙧𝙤𝙪𝙥", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ 𝘼𝙙𝙙 𝙈𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="⚙️ 𝙃𝙚𝙡𝙥 & 𝘾𝙈𝘿𝙎", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🎁 𝙎𝙤𝙪𝙧𝙘𝙚", callback_data="SOURCE"),
        InlineKeyboardButton(text="📝 𝘼𝙗𝙤𝙪𝙩", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="➕ 𝘼𝙙𝙙 𝙈𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="❌ 𝘾𝙡𝙤𝙨𝙚",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="⚡️ 𝘾𝙝𝙖𝙩-𝘽𝙤𝙩", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🔥 𝙏𝙤𝙤𝙡𝙨", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝙀𝙣𝙖𝙗𝙡𝙚", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝘿𝙞𝙨𝙖𝙗𝙡𝙚", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="𝙎𝙤𝙤𝙣..", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="SBACK"),
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="⚙️ 𝙃𝙚𝙡𝙥", callback_data="HELP"),
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="⚙️ 𝙃𝙚𝙡𝙥", url=f"https://t.me/{BOT_USERNAME}?start=help"
        ),
        InlineKeyboardButton(text="❌ 𝘾𝙡𝙤𝙨𝙚", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="💫 𝘾𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙂𝙧𝙤𝙪𝙥", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="👑 𝗢𝘄𝗻𝗲𝗿", user_id=OWNER),
        InlineKeyboardButton(text="🎁 𝙎𝙤𝙪𝙧𝙘𝙚", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="💎 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]
