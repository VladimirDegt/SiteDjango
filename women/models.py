from django.db import models
from django.urls import reverse


class Women(models.Model):  # название табл будет Women
    # поле id автоматически прописывается в Model
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи") # verbose_name для админ панели
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")  # это поле неизменяемое
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")  # это поле изменяемое при апдейте
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    # cat_id, id django автоматом добавляет
    """если загружается много файлов, то в photo делаем чтобы они распределялись по папкам по дате
     и в settings прописываем 2 переменные"""
    """для вывода по запросу Women.objects.all() всех титулов, а не объектов"""

    def __str__(self):
        return self.title

    # формирования нужных маршрутов для динам ссылок в данном случае для 'post'
    # reverse возвращает маршрут ввиде path("post/<int:post_id>" подставляя 'post_id'
    def get_absolute_url(self):  # так же наличие этой фук-ции добавляет "смотреть на сайте" в админ панели
        return reverse('post', kwargs={'post_slug': self.slug})
    # специальный класс для работы в админ панели с Women
    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"  # чтобы авто не добавляло "s" в конце
        ordering = ['time_create', 'title']  # сортировка

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
# db_index - поле будет индексировано, т.е. быстрее поиск по нему
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})