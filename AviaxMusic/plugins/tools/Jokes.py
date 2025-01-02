import requests 
import json
from YukkiMusic import app 
from pyrogram import client, filters 


@app.on_message(filters.command(["jokes", "joke"]))
async def jokes(client, message):
    try:
       X = requests.get("https://api.safone.dev/joke")
       Xy = X.json()
       Xyz = Xy.get("joke", "")
       await message.reply_text(Xyz)
    except Exception as e:
         print(e)
         await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ")



@app.on_message(filters.command(["meme", "memes"]))
async def random_memes(client, message):
    Url = "https://apis-awesome-tofu.koyeb.app/api/meme?type=random"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        media_type = data['contentType'].split('/')[0]
        media_url = data['media']
        await (message.reply_photo if media_type == 'image' else message.reply_video)(media_url, True)
    else:
        return await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ...")
