from tortoise import fields
from pydantic import Field
from tortoise.models import Model


class Book(Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=400)
    description = fields.CharField(max_length=400)
    condition: bool = Field(...)
    created_at = fields.DatetimeField(auto_now_add=True)
    
