# Overview
[Alembic](https://alembic.sqlalchemy.org/en/latest/) is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

### Usage
In order to create an environment using the “async” template execute `init` command.
`async` - generic single-database configuration with an async dbapi.
```zsh
alembic init -t async migrations
```

In order to autogenerate database migrations based on the existing models execute `revision` command.
```zsh
alembic revision --autogenerate -m "init"
```

We now want to run our migration. Assuming our database is totally clean, it’s as yet unversioned. The alembic upgrade command will run upgrade operations, proceeding from the current database revision, in this example None, to the given target revision. We can specify 1975ea83b712 as the revision we’d like to upgrade to, but it’s easier in most cases just to tell it “the most recent”, in this case head:
```zsh
alembic upgrade head
```
