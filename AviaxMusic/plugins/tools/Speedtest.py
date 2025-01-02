import speedtest
from pyrogram import Client, filters
from YukkiMusic import app 

@app.on_message(filters.command("speedtest"))
async def speedtest_command(client, message):
    msg = await message.reply_text("ʀᴜɴɴɪɴɢ ꜱᴘᴇᴇᴅᴛᴇꜱᴛ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")

    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()

        download_speed = results["download"] / 1_000_000  # Convert 
        upload_speed = results["upload"] / 1_000_000      # Convert to Mbps
        ping = results["ping"]

        await msg.edit_text(
            f"<u>**ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ꜱᴘᴇᴇᴅᴛᴇꜱᴛ ʀᴇꜱᴜʟᴛꜱ **</u>\n\n"
            f"**ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴘᴇᴇᴅ:** {download_speed:.2f} Mbps\n"
            f"**ᴜᴘʟᴏᴀᴅ ꜱᴘᴇᴇᴅ:** {upload_speed:.2f} Mbps\n"
            f"**ᴄᴜʀʀᴇɴᴛ ᴘɪɴɢ:** {ping} ms"
        )
    except Exception as e:
        await msg.edit_text(f"An error occurred: {e}")

