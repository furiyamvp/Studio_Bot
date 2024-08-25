from typing import Any, Union

from main.database import database
from main.models import *


async def get_user(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error get user with ID {chat_id}: {e}"
        print(error_text)


async def add_user(message):
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            suggested=0,
            created_at=message.date
        )
        print(2)
        await database.execute(query)
        return True
    except Exception as e:
        error_text = f"Error adding user: {e}"
        print(error_text)


async def update_suggested(chat_id: int, date) -> Union[dict[Any, Any], bool]:
    try:
        user_data = await get_user(chat_id)
        if not user_data:
            return False
        query = users.update().where(users.c.chat_id == chat_id).values(suggested=user_data["suggested"] + 1,
                                                                        updated_at=date).returning(users)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False

    except Exception as e:
        error_text = f"Error updating user's suggested with chat_id {chat_id}: {e}"
        print(error_text)
        return False


async def update_suggested_to_zero(chat_id: int, date) -> Union[dict[Any, Any], bool]:
    try:
        query = users.update().where(users.c.chat_id == chat_id).values(suggested=0, updated_at=date)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False

    except Exception as e:
        error_text = f"Error updating user's suggested with chat_id {chat_id}: {e}"
        print(error_text)
        return False


async def get_user_data(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        if row:
            return dict(row)
        else:
            return None
    except Exception as e:
        error_text = f"Error fetching user with ID {chat_id}: {e}"
        print(error_text)
        return None
