from lib2to3.pytree import Base
from pydantic import BaseModel


class DoneResponse(BaseModel):
  id: int
  
  class Config:
    orm_mode = True