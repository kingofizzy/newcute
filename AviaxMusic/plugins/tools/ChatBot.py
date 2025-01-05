from pyrogram import Client, filters, enums, types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from motor.motor_asyncio import AsyncIOMotorClient
import requests
from config import MONGO_DB_URI
from AviaxMusic import app

mongo_client = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo_client.chatbotdbb
chatbotdatabase = db.chatbotdbbb


async def is_admin(chat_id: int, user_id: int) -> bool:
    member = await app.get_chat_member(chat_id, user_id)
    return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]


@app.on_message(filters.command("chatbot") & filters.group, group=10)
async def chatbot_command(_, message: Message):
    if await is_admin(message.chat.id, message.from_user.id):

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Enable", callback_data="enable_chatbot"),
                    InlineKeyboardButton(text="Disable", callback_data="disable_chatbot"),
                ]
            ]
        )
        await message.reply_text("Choose an option:", reply_markup=keyboard)
    else:
        await message.reply_text("You are not an admin in this group.")



@app.on_callback_query(filters.regex(r"^(enable|disable)_chatbot$"))
async def enable_disable_chatbot(_, query: types.CallbackQuery):
    chat_id = query.message.chat.id
    action = query.data

    if await is_admin(chat_id, query.from_user.id):
        if action == "enable_chatbot":
            if await chatbotdatabase.find_one({"chat_id": chat_id}):
                await query.answer("Chatbot is already enabled.", show_alert=True)
            else:
                await chatbotdatabase.insert_one({"chat_id": chat_id, "admin_id": query.from_user.id})
                await query.answer("Chatbot enabled successfully!", show_alert=True)
                await query.message.edit_text(f"Chatbot enabled by {query.from_user.mention()}")
        else:
            chatbot_info = await chatbotdatabase.find_one({"chat_id": chat_id})
            if chatbot_info:
                await chatbotdatabase.delete_one({"chat_id": chat_id})
                await query.answer("Chatbot disabled successfully!", show_alert=True)
                await query.message.edit_text("Chatbot disabled.")
            else:
                await query.answer("Chatbot is not enabled for this chat.", show_alert=True)
    else:
        await query.answer("You are not an admin in this group.", show_alert=True)

import requests
from urllib.parse import urlencode
from pyrogram import Client, filters, enums
from pyrogram.types import Message

@app.on_message(filters.text & filters.group, group=10)
async def handle_message(client: Client, message: Message):
    try:
        chat_id = message.chat.id

        if (message.reply_to_message and message.reply_to_message.from_user.is_self) or not message.reply_to_message:
            chatbot_info = await chatbotdatabase.find_one({"chat_id": chat_id})
            if chatbot_info:
                user_message = message.text
                await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)

                
                base_url = "https://gpt.hazex.workers.dev/"
                query_params = {'ques': user_message}
                api_url = f"{base_url}?{urlencode(query_params)}"

                
                try:
                    response = requests.get(api_url)
                    if response.status_code == 200:
                        api_response = response.json()
                        if 'answer' in api_response:
                            await message.reply_text(api_response['answer'])
                        else:
                            await message.reply_text("Sorry, I couldn't generate a response.")
                    else:
                        await message.reply_text("Failed to connect to the AI service.")
                except Exception as e:
                    print(f"Error fetching response: {e}")
                    await message.reply_text("An error occurred while processing your request.")
            else:
                pass
    except Exception as e:
        print(e)
