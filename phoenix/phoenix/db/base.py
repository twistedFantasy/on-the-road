# Import all the models, so that Base has them before being
# imported by Alembic
from phoenix.db.base_class import Base  # noqa
from phoenix.users.models import User  # noqa
