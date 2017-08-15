import datetime

from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects.mysql import LONGTEXT, TIMESTAMP, INTEGER

from app import db


class TodoModel(db.Model):
    __tablename__ = 'todo'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    status_enum = ('pending', 'resolve', 'deleted')

    id = Column(
        INTEGER(20, unsigned=True),
        primary_key=True
    )
    content = Column(
        LONGTEXT,
        nullable=False
    )
    status = Column(
        Enum(*status_enum),
        default=status_enum[0],
        nullable=False
    )
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow
    )

