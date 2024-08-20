import sqlalchemy
from datetime import datetime

from main.config import tashkent_tz
from main.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("suggested", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=datetime.utcnow)
)
