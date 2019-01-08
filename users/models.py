from django.db import models
from enum import Enum


class RoleType(Enum):
    ANALYZER = 10
    WASHER = 30


class User(models.Model):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField(default=3, choices=((RoleType.WASHER.value, "标注员"), (RoleType.ANALYZER.value, "分析师"),))
    create_time = models.DateTimeField(auto_now_add=True)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'role': self.role,
        }

