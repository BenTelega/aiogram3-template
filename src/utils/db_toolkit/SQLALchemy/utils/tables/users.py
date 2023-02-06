from ....db_toolkit import *
from ..databases import *

class Users(Helper, DateHelper):
	def __init__(self, database: Database) -> None:
		Helper.__init__(self)
		DateHelper.__init__(self)

		self.table = database.users
		self.db = database
	
	async def add(self, user_id: int):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				insert(self.table).values(
					user_id=user_id,
					reg_date=self.get_timestamp(self.get_date_now())
				).returning(self.table)
			)

			await conn.commit()

			return data.fetchone()
	
	async def get_one_by_user_id(self, user_id: int):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				select(self.table).where(
					self.table.c.user_id == user_id
				)
			)

			return data.fetchone()
	
	async def get_many_by_id(self, user_ids: List[int]):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				select(self.table).where(
					self.table.c.user_id.in_(user_ids)
				)
			)

			return data.fetchall()

	
	async def get_all(self):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				select(self.table)
			)

			return data.fetchall()

	async def set_field(self, user_id: int, fields: Dict[str, Any]):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				update(self.table).where(
					self.table.c.user_id == user_id
				).values(
					fields
				).returning(self.table)
			)

			await conn.commit()

			return data.fetchone()

	async def delete(self, user_ids: List[int]):
		async with self.db.engine.connect() as conn:
			data = await conn.execute(
				delete(self.table).where(
					self.table.c.user_id.in_(user_ids)
				).returning(self.table)
			)

			await conn.commit()

			return data.fetchall()