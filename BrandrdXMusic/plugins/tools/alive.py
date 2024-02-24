import asyncio
from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_photo(
            photo=config.ALIVE_IMG_URL,
        caption=f"<b>ʜᴇʏ</b> {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ ᴀʟɪᴠᴇ!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Girls_Group_And_Chatting_Boys"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
