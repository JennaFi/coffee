from django.db import models
from django.urls import reverse


class Coffee(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = ('id', 'slug',)
        verbose_name = 'coffee'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:coffee',
                       args=[self.id, self.slug, self.image])


class Tea(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = ('id', 'slug',)
        verbose_name = 'tea'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:tea',
                       args=[self.id, self.slug])

