from django.db import models


# Create your models here.


class FaceitPost(models.Model):
    date = models.DateTimeField()
    json_body = models.TextField(max_length=20000)

    def __str__(self):
        return self.json_body