"""Database module."""

from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging

from sqlalchemy import create_engine, orm
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session ,declarative_base

logger = logging.getLogger(__name__)

Base = declarative_base()

class Database:

    def __init__(self, connectionstring: str) -> None:
        self._engine = create_engine(connectionstring, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )
        self.create_database()

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            # session.query(AccountEntity).update()
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()