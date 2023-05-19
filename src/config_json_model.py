from pydantic import BaseModel

class Config(BaseModel):
    admins: list[int]