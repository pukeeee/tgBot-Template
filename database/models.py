from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from app.core.utils.config import DB_URL


engine = create_async_engine(
    url=DB_URL,
    echo=True,
    pool_pre_ping=True
)


async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Example(Base):
    __tablename__ = "example"



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)