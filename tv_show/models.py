from django.db import models

class Movies(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
    )
    image = models.ImageField(upload_to='movies/', verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='напишите название фильма')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=400)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, 
                                     verbose_name='выберите жанр')
    time_watch = models.PositiveIntegerField(default=120, 
                                             verbose_name='Укажите время фильма')
    director = models.CharField(max_length=100, verbose_name='Укажите режисера', 
                                default='Иван Иванов')
    trailer = models.URLField(verbose_name='укажите ссылку с YOUTUBE')

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'список фильмов'

    def __str__(self):
        return f'{self.title} - {self.price} сом'
