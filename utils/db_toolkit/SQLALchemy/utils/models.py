from sqlalchemy import MetaData, Table, Column
from sqlalchemy.dialects import postgresql 


class Users:
    '''Postgres Model'''

    def __init__(self, metadata: MetaData) -> None:
        self.name = 'users'
        self.metadata = metadata

    def get_table(self) -> Table:
        return Table(self.name, self.metadata,
            Column('id', postgresql.INTEGER(), primary_key=True),
            Column('user_id', postgresql.BIGINT(32), index=True),
            Column('reg_date', postgresql.BIGINT()),
        )
