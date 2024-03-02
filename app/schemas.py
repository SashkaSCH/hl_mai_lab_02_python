from pydantic import BaseModel, EmailStr, Field


class UserIn(BaseModel):
    login: str = Field(..., max_length=256)
    password: str = Field(..., max_length=256)


class UserOut(BaseModel):
    id: int
    login: str = Field(..., max_length=256)
    first_name: str | None = Field(None, max_length=256)
    last_name: str | None = Field(None, max_length=256)
    birth_date: str | None = Field(None, format="date")
    email: EmailStr | None = Field(None, max_length=256)
    title: str | None = Field(None, max_length=256)
    photo: str | None = Field(None, max_length=256)


class WallCreate(BaseModel):
    content: str = Field(..., max_length=256)
    user_id: int


class WallOut(BaseModel):
    wall_id: int
    content: str = Field(..., max_length=256)
    user: UserOut


class MessageCreate(BaseModel):
    content: str = Field(..., max_length=256)
    author_id: int
    recipient_id: int


class MessageOut(BaseModel):
    message_id: int
    content: str = Field(..., max_length=256)
    author: UserOut
    recipient: UserOut
