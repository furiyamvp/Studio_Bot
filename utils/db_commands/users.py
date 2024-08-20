from datetime import datetime
from typing import Any, Union

from main.config import tashkent_tz
from main.database import database
from main.models import users


async def get_user(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error get user with ID {chat_id}: {e}"
        print(error_text)


async def get_user_with_id(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error get user with ID {chat_id}: {e}"
        print(error_text)
        return False


async def update_user_suggested(chat_id: int, date):
    try:
        query = users.update().where(users.c.chat_id == chat_id).values(suggested=users.c.suggested + 1,
                                                                        updated_at=date)
        await database.execute(query)
    except Exception as e:
        error_text = f"Error updating user with ID {chat_id}: {e}"
        print(error_text)


async def add_user(chat_id: int, date):
    try:
        query = users.insert().values(
            chat_id=chat_id,
            suggested=0,
            created_at=date
        )
        await database.execute(query)
    except Exception as e:
        error_text = f"Error adding user with ID {chat_id}: {e}"
        print(error_text)
