from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base

class ToDo(Base):
    __tablename__ = "ToDos"
    
    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, index=True)
    status = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    