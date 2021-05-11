from django.db import models


# Create your models here.
class Table(models.Model):
    person_name = models.CharField(max_length=100, default=0, blank=False, null=False)
    mob_number = models.CharField(max_length=10, default=0, blank=False, null=False)
    members = models.CharField(max_length=2, default=0, blank=False, null=False)
    remain_tables = models.IntegerField(max_length=2, default=12, blank=False, null=False)

    def __str__(self):
        return self.person_name
