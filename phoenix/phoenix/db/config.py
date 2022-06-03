import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

TESTING = os.getenv("TESTING", default=False)

host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")

if TESTING:
    if db:
        db += "_test"
    else:
        db = "default_db"

Base = declarative_base()

engine = create_async_engine(f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}", future=True, echo=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session
