from django.db import models

# Create your models here.


class todoData(models.Model):
    title = models.CharField("Title", max_length=255, blank=True, null=True)
    done = models.BooleanField("Done", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
