from django.db import models


class DomainPropertyCache(models.Model):
    cache_key = models.CharField(max_length=250, primary_key=True)
    value = models.CharField(max_length=250, null=False)
    expires = models.DateTimeField(max_length=250, null=False, db_index=True)

