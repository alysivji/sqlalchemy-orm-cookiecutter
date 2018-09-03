from sqlalchemy_wrapper import SQLAlchemy

from .config import DATABASE_URI


db: SQLAlchemy = SQLAlchemy(DATABASE_URI)
from app import models  # noqa
