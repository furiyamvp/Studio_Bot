from main.database import database
from main.models import account

import random
from sqlalchemy import select, update


async def get_account_data(date):
    try:
        query = select(account).where(account.c.quantity_players < 5)
        accounts = await database.fetch_all(query)

        if accounts:
            selected_user = random.choice(accounts)
            update_query = (
                update(account)
                .where(account.c.id == selected_user["id"])
                .values(quantity_players=account.c.quantity_players + 1, updated_at=date)
                .returning(account)
            )
            row = await database.fetch_one(update_query)
            return dict(row) if row else "None"
        else:
            return "None"
    except Exception as e:
        error_text = f"Error updating quantity_players: {e}"
        print(error_text)
        return False


async def add_account(data: dict):
    try:
        query = account.insert().values(
            email=data.get("email"),
            password=data.get("password"),
            status="active",
            quantity_players=0,
            created_at=data.get('created_at')
        ).returning(account.c.id)
        return await database.execute(query)

    except Exception as e:
        error_text = f"Error adding account: {e}"
        print(error_text)
        return None
