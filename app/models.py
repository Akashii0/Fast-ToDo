from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from database import Base

class ToDo(Base):
    __tablename__ = "ToDos"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, index=True)
    status = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    