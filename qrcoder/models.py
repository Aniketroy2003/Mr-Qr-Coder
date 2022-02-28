from django.db import models

# Create your models here.
class Search(models.Model):
    searched = models.TextField()
    time_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searched