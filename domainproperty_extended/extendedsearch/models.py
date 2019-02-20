from django.db import models


class DomainPropertyCache(models.Model):
    # OAuth token storage
    cache_key = models.CharField(max_length=250, primary_key=True)
    value = models.CharField(max_length=250, null=False)
    expires = models.DateTimeField(max_length=250, null=False, db_index=True)


class SortKey(models.Model):

    DEFAULT = 'Default'
    PRICE = 'Price'
    DATE_UPDATED = 'DateUpdated'
    CHOICES = (
        ('Default', 'Default'),
        ('Price', 'Price'),
        ('DateUpdated', 'Date Updated')
    )
    sort_choices = models.CharField(
        max_length=20,
        choices=CHOICES,
        default=DEFAULT
    )

    def __str__(self):
        return self.sort_choices
