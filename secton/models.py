from django.db import models


class SectionGroup(models.Model):
    section_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class Section(models.Model):
    group = models.ForeignKey(SectionGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    people_count = models.IntegerField(default=0, max_length=100)