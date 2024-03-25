from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)