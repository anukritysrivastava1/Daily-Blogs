from django.db import models

# Create your models here.
class Post(models.Model):
    Sno=models.AutoField(primary_key=True)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    slug=models.CharField(max_length=14)
    Timestamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return "Posted By " + self.author + " - " + self.title