from YukkiMusic.core.mongo import mongodb

welcomedb = mongodb.welcome


async def get_welcome(chat_id: int) -> (str, str, str):
    data = await welcomedb.find_one({"chat_id": chat_id})
    if not data:
        return "", "", ""

    welcome = data.get("welcome", "")
    raw_text = data.get("raw_text", "")
    file_id = data.get("file_id", "")

    return welcome, raw_text, file_id


async def set_welcome(chat_id: int, welcome: str, raw_text: str, file_id: str):
    update_data = {
        "welcome": welcome,
        "raw_text": raw_text,
        "file_id": file_id,
    }

    return await welcomedb.update_one(
        {"chat_id": chat_id}, {"$set": update_data}, upsert=True
    )


async def del_welcome(chat_id: int):
    return await welcomedb.delete_one({"chat_id": chat_id})
