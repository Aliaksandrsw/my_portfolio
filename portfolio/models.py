from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100,verbose_name= 'Заголовок')
    description = models.CharField(max_length=250, verbose_name= 'Описание')
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'