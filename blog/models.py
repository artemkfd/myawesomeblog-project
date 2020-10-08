from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.title

    def get_summary(self):
        sum_text = self.text[:70] + '...'
        return sum_text