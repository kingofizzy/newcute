import os 
import random
from Yukki import Owner
import asyncio
from PIL import Image , ImageDraw
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from AviaxMusic import app
from pyrogram.enums import ChatAction, ChatType


@app.on_message(
   filters.command(["couples", "couple"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def couples(app, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")
    try:
         xyz = message.from_user.mention
         msg = await message.reply_text("🌷")
         list_of_users = []

         async for i in app.get_chat_members(message.chat.id, limit=50):
             if not i.user.is_bot:
               list_of_users.append(i.user.id)

         c1_id = random.choice(list_of_users)
         c2_id = random.choice(list_of_users)
         while c1_id == c2_id:
              c1_id = random.choice(list_of_users)


         photo1 = (await app.get_chat(c1_id)).photo
         photo2 = (await app.get_chat(c2_id)).photo

         N1 = (await app.get_users(c1_id)).mention 
         N2 = (await app.get_users(c2_id)).mention

         try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
         except Exception:
            p1 = "assets/C/coupless.png"
         try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
         except Exception:
            p2 = "assets/C/coupless.png"
         

         img1 = Image.open(f"{p1}")
         img2 = Image.open(f"{p2}")
         xy = ["Zero1", "Zero2", "Zero3"]
         x = random.choice(xy)

         img = Image.open(f"assets/C/{x}.png")

         img1 = img1.resize((680,680))
         img2 = img2.resize((680,680))

         mask = Image.new('L', img1.size, 0)
         draw = ImageDraw.Draw(mask) 
         draw.ellipse((0, 0) + img1.size, fill=255)

         mask1 = Image.new('L', img2.size, 0)
         draw = ImageDraw.Draw(mask1) 
         draw.ellipse((0, 0) + img2.size, fill=255)


         img1.putalpha(mask)
         img2.putalpha(mask1)

         draw = ImageDraw.Draw(img)

         img.paste(img1, (185, 359), img1)
         img.paste(img2, (1696, 359), img2)

         img.save(f'test_{cid}.png')

         TXT = f"""
**<u>ʀᴀɴᴅᴏᴍ  sᴇʟᴇᴄᴛᴇᴅ ᴄᴏᴜᴘʟᴇs ❣️:</u>**

{N1} + {N2} = ❣️


||ʀᴇǫᴜᴇsᴛᴇᴅ Bʏ - {xyz}||


"""
         await app.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
         await message.reply_photo(f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(
                [
       [
            InlineKeyboardButton(
                text="ʀᴇꜰʀᴇꜱʜ ",    
                callback_data="coupless",
            )
        ]
]

              ),)
         await msg.delete()
    except Exception as e:
        print(str(e))
    try:
      os.remove(f"./downloads/pfp1.png")
      os.remove(f"./downloads/pfp2.png")
      os.remove(f"test_{cid}.png")
    except Exception:
       pass







@app.on_callback_query(filters.regex("coupless"))
async def regeneratecouples(client: Client, cb: CallbackQuery):
    uid = cb.from_user.id
    chat = cb.message.chat
    xyz = cb.from_user.mention
    list_of_users = []
    
    if uid in Owner:
        pass
    else:
        member = await chat.get_member(uid)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            pass
        else:
            await cb.answer("ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ !", show_alert=True)

    async for i in app.get_chat_members(cb.message.chat.id, limit=90):
        if not i.user.is_bot:
            list_of_users.append(i.user.id)

    c1_id = random.choice(list_of_users)
    c2_id = random.choice(list_of_users)
    while c1_id == c2_id:
        c1_id = random.choice(list_of_users)

    photo1 = (await app.get_chat(c1_id)).photo
    photo2 = (await app.get_chat(c2_id)).photo

    N1 = (await app.get_users(c1_id)).mention
    N2 = (await app.get_users(c2_id)).mention

    try:
       p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
    except Exception:
        p1 = "assets/C/coupless.png"
    try:
       p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
    except Exception:
        p2 = "assets/C/coupless.png"

    img1 = Image.open(p1)
    img2 = Image.open(p2)
    xy = ["Zero1", "Zero2", "Zero3"]
    x = random.choice(xy)

    img = Image.open(f"assets/C/{x}.png")

    img1 = img1.resize((680, 680))
    img2 = img2.resize((680, 680))

    mask = Image.new('L', img1.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img1.size, fill=255)

    mask1 = Image.new('L', img2.size, 0)
    draw = ImageDraw.Draw(mask1)
    draw.ellipse((0, 0) + img2.size, fill=255)

    img1.putalpha(mask)
    img2.putalpha(mask1)

    draw = ImageDraw.Draw(img)

    img.paste(img1, (185, 359), img1)
    img.paste(img2, (1696, 359), img2)

    cid = cb.message.chat.id
    img.save(f'test_{cid}.png')

    TXT = f"""
**<u>ʀᴀɴᴅᴏᴍ  sᴇʟᴇᴄᴛᴇᴅ ᴄᴏᴜᴘʟᴇs ❣️:</u>**

{N1} + {N2} = ❣️


||ʀᴇǫᴜᴇsᴛᴇᴅ Bʏ - {xyz}||


"""
    await app.send_chat_action(cid, ChatAction.UPLOAD_PHOTO)
    await cb.message.reply_photo(f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ʀᴇꜰʀᴇꜱʜ",
                    callback_data="coupless",
                )
            ]
        ]
    ))

    try:
        os.remove("pfp.png")
        os.remove("pfp1.png")
        os.remove(f"test_{cid}.png")
    except Exception:
        pass
