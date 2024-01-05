from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """**
ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴋʏᴀ 😂🤡
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AKHANDBHARRAT"),
          InlineKeyboardButton("🥀ᴏᴡɴᴇʀ🍃", url="https://t.me/About_SAII"),
          ],
               [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/SHAYRI_W0RLD"),

],
[
              InlineKeyboardButton("˹ᴀиσx ꭙ ѕραмᴇꝛ˼", url=f"https://t.me/ANOX_SPAMBOT?startgroup=true"),
              InlineKeyboardButton("︎˹ᴀиσx ꭙ ᴍᴜꜱɪᴄ˼", url=f"https://t.me/ANOX_MUSICBOT?startgroup=true"),
              ],
              [
              InlineKeyboardButton("ʀᴇᴘᴏ", url=f"https://telegra.ph/file/78be765f35211e764a9d5.mp4"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/2e54b26019680225ea7f1.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
