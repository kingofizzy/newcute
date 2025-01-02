from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
import time
from Yukki import Owner
import datetime
from collections import defaultdict
from YukkiMusic import app


message_counts = defaultdict(list)

@app.on_message(filters.group, group=50)
async def anti_spam(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    

    current_time = time.time()
    message_counts[user_id] = [timestamp for timestamp in message_counts[user_id] if current_time - timestamp <= 5]
    message_counts[user_id].append(current_time)

    if len(message_counts[user_id]) > 7:
        if user_id in Owner:
            return
        member = await client.get_chat_member(chat_id, user_id)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            text = f"{message.from_user.mention} ɪꜱ ꜱᴘᴀᴍᴍɪɴɢ \n\nᴀᴄᴛɪᴏɴ - ɪ ᴄᴀɴᴛ ᴅᴏ ᴀɴʏᴛʜɪɴɢ \nʀᴇᴀꜱᴏɴ - ᴜꜱᴇʀ ɪꜱ ᴀɴ ᴀᴅᴍɪɴ "
            admin_data = [
                i async for i in client.get_chat_members(
                    chat_id=chat_id,
                    filter=enums.ChatMembersFilter.ADMINISTRATORS
                )
            ]
            for admin in admin_data:
                if admin.user.is_bot or admin.user.is_deleted:
                    continue
                text += f"[\u2063](tg://user?id={admin.user.id})"
            await client.send_message(chat_id, text)
            return 
        
        mute_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
        await app.restrict_chat_member(chat_id, user_id, ChatPermissions(), until_date=mute_time)
        
        button = [
            [
                InlineKeyboardButton(
                    text=" ᴜɴᴍᴜᴛᴇ ",
                    callback_data=f"unmute_={user_id}",
                ),
                InlineKeyboardButton(
                    text=" ᴅᴇʟᴇᴛᴇ ",
                    callback_data=f"close",
                ),
            ]
        ]
        await message.reply_text(
            f"{message.from_user.mention} ɪꜱ ꜱᴘᴀᴍᴍɪɴɢ \n\nᴀᴄᴛɪᴏɴ - ᴍᴜᴛᴇᴅ\nᴛɪᴍᴇ - 5 ᴍɪɴᴜᴛᴇꜱ",
            reply_markup=InlineKeyboardMarkup(button)
        )
        
        message_counts[user_id] = []

