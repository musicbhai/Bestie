from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - Sɪʟᴇɴᴛʜʀᴀx
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - Sɪʟᴇɴᴛʜʀᴀx
│├─────────────────╯
├┼─────────────────⦿
├┤~ @ABOUT_SILENTHRAX
├┤~ @BESTIE_UNITE_CLUB
├┤~ @silenthrex
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @silenthrax
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Aura", url=f"https://t.me/Usesense")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/AuraVisual"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/HeavenChatGroup"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/AuraVisual"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/RJ_92_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/qu0hhu.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
