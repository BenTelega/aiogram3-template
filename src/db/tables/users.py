from db.database import Session
# from db_models.models import Users

from sqlalchemy import select, update
from datetime import datetime

async def add(
    user_id: int,
    full_name: str,
    username: str,
):
    async with Session() as conn:
        result = conn.add(Users(
            user_id=user_id,
            full_name=full_name,
            username=username,
            reg_date=datetime.now().timestamp()
        ))
        
        await conn.commit()

        return result

async def get_one_by_id(id: int):
    async with Session() as conn:
        return await conn.get(Users, id)

async def get_one_by_user_id(id: int):
    async with Session() as conn:
        return (await conn.execute(
            select(Users).where(
                Users.user_id == id
            )
        )).scalar()

async def get_all():
    async with Session() as conn:
        return (await conn.execute(select(Users))).scalars().all()

async def set_field_by_id(id: int, fields: dict):
    async with Session() as conn:
        result = await conn.execute(
            update(Users).values(
                **fields
            ).where(
                Users.id == id
            )
        )

        await conn.commit()

        return result
