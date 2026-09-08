from tortoise import fields
from tortoise.models import Model


class Student(Model):
    id = fields.IntField(primary_key=True)
    no = fields.CharField(max_length=255, null=True)
    name = fields.CharField(max_length=255, null=True)
    clazz = fields.CharField(max_length=255, null=True)
    major = fields.CharField(max_length=255, null=True)
    college = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, null=True)
    address = fields.CharField(max_length=255, null=True)

    class Meta:
        table_name = 'student'

