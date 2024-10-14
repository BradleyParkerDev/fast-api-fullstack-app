from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba991374cd4d'
down_revision: Union[str, None] = '6f056ad8a170'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename the 'id' column to 'user_id'
    op.alter_column('users', 'id', new_column_name='user_id')
    
    # Drop and recreate foreign key in user_sessions that references user_id
    op.drop_constraint('user_sessions_user_id_fkey', 'user_sessions', type_='foreignkey')
    op.create_foreign_key(None, 'user_sessions', 'users', ['user_id'], ['user_id'], ondelete='CASCADE')


def downgrade() -> None:
    # Reverse the rename of 'user_id' back to 'id'
    op.alter_column('users', 'user_id', new_column_name='id')
    
    # Drop and recreate the original foreign key in user_sessions referencing 'id'
    op.drop_constraint(None, 'user_sessions', type_='foreignkey')
    op.create_foreign_key('user_sessions_user_id_fkey', 'user_sessions', 'users', ['user_id'], ['id'])
