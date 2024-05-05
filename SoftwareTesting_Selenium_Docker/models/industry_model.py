from django.db import models

class IndustryModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    CreateAt = models.DateTimeField(auto_now_add=True)