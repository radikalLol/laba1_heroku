from django.db import models

# Create your models here.
class Artical(models.Model):
    class Meta:
        db_table =  "Article"
    artical_title = models.CharField(max_length=20)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField()
