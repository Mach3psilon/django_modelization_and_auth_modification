from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Ebook(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=120, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return self.review 