import sqlalchemy
from datetime import datetime

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

account = sqlalchemy.Table(
    "account",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("quantity_players", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=datetime.utcnow)
)
