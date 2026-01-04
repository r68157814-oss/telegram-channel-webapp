from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    is_admin: bool = False
    is_paid: bool = False
