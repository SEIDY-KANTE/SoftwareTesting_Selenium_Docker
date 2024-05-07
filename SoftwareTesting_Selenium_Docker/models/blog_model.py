from django.db import models


class BlogModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Image = models.CharField(max_length=50)
    Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Content = models.TextField()
    CreateAt = models.DateTimeField(auto_now_add=True)
