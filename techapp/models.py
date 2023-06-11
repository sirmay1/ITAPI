from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' | ' + self.paradigm + ' | ' + self.category + ' | ' + str(self.detail)
