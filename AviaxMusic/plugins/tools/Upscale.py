from YukkiMusic import app
from pyrogram import Client, filters
import base64
import requests
import os
from pyrogram.enums import ChatAction
from config import LOG_GROUP_ID

@app.on_message(filters.command(["enhance", "upscale"]))
async def enhance(_, message):
    reply = message.reply_to_message
    user_id = message.from_user.id

    if not reply or (not reply.photo and not reply.sticker):
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ....😑")
    else:
        path = await reply.download(
            file_name=f"{user_id}.jpeg"
        )

        msg = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ......")
        with open(path, 'rb') as file:
            photo = file.read()

        encoded_image_data = base64.b64encode(photo).decode('utf-8')

        url = 'https://apis-awesome-tofu.koyeb.app/api/remini?mode=enhance'
        headers = {
            'accept': 'image/jpg',
            'Content-Type': 'application/json'
        }
        data = {
            "imageData": encoded_image_data
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data
            )
            await msg.edit(
                "ᴀʟᴍᴏsᴛ ᴅᴏɴᴇ......❣️"
            )

            path = f"@itz_cute_shivani_upscaled_{user_id}.png"

            with open(path, 'wb') as file:
                file.write(response.content)
            await app.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            if await message.reply_document(
                document=path, quote=True
            ):
                await msg.delete()

            os.remove(path)

        except Exception as e:
            await app.send_message(LOG_GROUP_ID, f"an error occured in upscale \n\n{e}")
            await message.reply_text(
                "ꜱᴏʀʀʏ ᴛᴏᴅᴀʏ ꜱᴇʀᴠᴇʀ ɪꜱ ᴅᴇᴀᴅ ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴛᴏᴍᴏʀʀᴏᴡ 😴"
            )
            return

