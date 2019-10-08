from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.


class Category(models.Model):
    STATUS = (
        (1, 'Doğru'),
        (0, 'Yanlış'),
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.IntegerField(choices=STATUS)
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.title]

        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return '->'.join(full_path[::-1])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.IntegerField()
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)
