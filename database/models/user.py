from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_image: str
    first_name: str
    last_name: str
    email_address: str
    user_name: str
    password: str
    last_updated: datetime = Field(default_factory=datetime.utcnow, nullable = False)







# class User(SQLModel, table=True):
#     id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)  # UUID v4 primary key
#     user_image: Optional[str] = None  # Optional field for user image
#     first_name: str = Field(nullable=False)  # Not nullable text field
#     last_name: str = Field(nullable=False)  # Not nullable text field
#     email_address: str = Field(unique=True, nullable=False)  # Unique and not nullable
#     user_name: str = Field(unique=True, nullable=False)  # Unique and not nullable
#     password: str = Field(nullable=False)  # Not nullable password field
#     last_updated: datetime = Field(default_factory=datetime.utcnow, nullable=False)  # Automatically sets current timestamp
