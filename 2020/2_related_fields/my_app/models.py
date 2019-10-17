from django.db import models
from django.utils import timezone

class Magazine(models.Model):
    issue = models.IntegerField()
    published = models.DateTimeField(default=timezone.now)

    def get_related_items(self):
        response = []
        for rel_obj in self._meta.related_objects:
            response += [
                instance
                for instance in rel_obj.related_model.objects.filter(
                    magazine = self
                )
            ]
        return response

class Article(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=127)
    text = models.TextField()

class Advertisement(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=127)
    text = models.TextField()

class Image(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    image = models.ImageField()
