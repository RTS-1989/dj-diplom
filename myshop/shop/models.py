from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='наименование')
    slug = models.SlugField(max_length=100, unique=True,
                            default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Subcategory(models.Model):
    category = models.ForeignKey('Category', related_name='subcategory',
                                 on_delete=models.PROTECT, default=None)
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='наименование')
    slug = models.SlugField(max_length=100, unique=True,
                            default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(
        'Subcategory', related_name='products',
        on_delete=models.CASCADE, verbose_name='подкатегория',
        default=None
    )
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='наименование')
    slug = models.SlugField(max_length=100, db_index=True,
                            default=None)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='цена')
    available = models.BooleanField(default=True, verbose_name='в наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Rating(models.Model):
    def __str__(self):
        return ()


class Review(models.Model):

    name = models.CharField('Имя', max_length=100, default=None)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='reviews',
                                verbose_name='Продукт', default=None)
    text = models.TextField('Сообщение', max_length=2000)
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан', null=True)
    parent = models.ForeignKey('self', verbose_name='Родитель',
                               on_delete=models.SET_NULL, blank=True,
                               null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} - {self.product}'
