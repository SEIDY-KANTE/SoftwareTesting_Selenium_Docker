from django.db import models


class IndustryModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    ListItems = models.TextField()
    Image = models.CharField(max_length=50)
    HistorySubTitle = models.CharField(max_length=100)
    HistoryTitle = models.CharField(max_length=100)
    HistoryTimeLineYear = models.CharField(max_length=25)
    HistoryTimeLineDescription = models.TextField(max_length=250)
    CreateAt = models.DateTimeField(auto_now_add=True)