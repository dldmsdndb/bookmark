from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름: " + self.site_name + " / 주소: " + self.url

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])
    