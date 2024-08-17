from django.db import models

class KindleBook(models.Model):
    asin = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    sold_by = models.CharField(max_length=255)
    img_url = models.URLField(max_length=500)
    product_url = models.URLField(max_length=500)
    stars = models.FloatField()
    price = models.FloatField()
    is_kindle_unlimited = models.BooleanField()
    category_id = models.IntegerField()
    is_best_seller = models.BooleanField()
    is_editors_pick = models.BooleanField()
    is_good_reads_choice = models.BooleanField()
    published_date = models.DateField()
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
