from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=60, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=120, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рубрику'
        verbose_name_plural = 'Рубрики'
        ordering = ('name',)


