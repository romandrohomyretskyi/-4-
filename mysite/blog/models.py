from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів.')
    slug = models.SlugField('Слаг')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            return reverse('articles-category-list', kwargs={'slug': self.slug})
        except:
            return '/'
        

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Опис')
    pub_date = models.DateTimeField('Дата публікації')
    slug = models.SlugField('Слаг')
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    main_page = models.BooleanField('Показувати на головній', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={
            'year': self.pub_date.year,
            'month': f'{self.pub_date.month:02}',
            'day': f'{self.pub_date.day:02}',
            'slug': self.slug
        })


class Image(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.article.title}"
