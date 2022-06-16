from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    author = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField(null=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)
    book_id = models.IntegerField(default=1)
