from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr  # Generate __tablename__ automatically
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
