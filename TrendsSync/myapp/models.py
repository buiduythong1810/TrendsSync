from django.db import models

class GoogleTrend(models.Model):
    stt = models.CharField(default="", max_length=8)
    noidung = models.CharField(default="", max_length=255)
# Create your models here.

class MyData(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)  # Thêm trường tên viết tắt

    def __str__(self):
        return self.name

class ggTrendsDailyData(models.Model):
    content = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


    def __str__(self):
        return self.content
    
class ggTrendsRealtimeData(models.Model):
    content = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


    def __str__(self):
        return self.content