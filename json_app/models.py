from django.db import models


class JsonModel(models.Model):
    json = models.JSONField()
