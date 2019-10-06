from django.db import models
from datetime import datetime, date, time
import django_tables2 as tables
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django.dispatch import receiver
from django.db.models.signals import post_save

# As model field:
from django_currentuser.db.models import CurrentUserField

# справочники
class type_eq(models.Model): # тип оборудования
    name=models.CharField(max_length=20, verbose_name=u'Тип оборудования')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name

class dep(models.Model): # отделение
    name=models.CharField(max_length=20, verbose_name=u'Отделение')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name

class ter(models.Model): # территория
    name=models.CharField(max_length=20, verbose_name=u'Территория')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name

class bild(models.Model): # здание
    name=models.CharField(max_length=20, verbose_name=u'Корпус')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name

class status(models.Model): # статус
    name=models.CharField(max_length=20, verbose_name=u'Статус')
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name

# оборудование
class equipment(models.Model):
    type=models.ForeignKey(type_eq, on_delete=None, null=False, default='')
    name=models.CharField(max_length=20, verbose_name=u'Модель')
    ter=models.ForeignKey(ter, on_delete=None, null=False, default='', verbose_name=u'Территория')
    dep=models.ForeignKey(dep, on_delete=None, null=False, default='', verbose_name=u'Отделение')
    bild=models.ForeignKey(bild, on_delete=None, null=False, default='', verbose_name=u'Корпус')
    status = models.ForeignKey(status, on_delete=None, null=False, default='', verbose_name=u'Статус')
    note=models.CharField(max_length=50, null=True, default='', verbose_name=u'Примечание' )
    dt=models.DateTimeField(default=datetime.now, verbose_name=u'Дата изменения')
    #author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Создал')
    created_by = CurrentUserField()


    def get_absolute_url_update(self):
        return "/edit/%i/" % self.id
    def get_absolute_url_delete(self):
        return "/delete/%i/" % self.pk
    def get_absolute_url_read(self):
        return "/read/%i/" % self.pk
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['type']

# история
class history(models.Model):
    id_eq=models.ForeignKey(equipment, on_delete=None, null=False, default='')
    type=models.ForeignKey(type_eq, on_delete=None, null=False, default='')
    name=models.CharField(max_length=20, verbose_name=u'Модель')
    ter=models.ForeignKey(ter, on_delete=None, null=False, default='')
    dep=models.ForeignKey(dep, on_delete=None, null=False, default='')
    bild=models.ForeignKey(bild, on_delete=None, null=False, default='')
    status = models.ForeignKey(status, on_delete=None, null=False, default='')
    note=models.CharField(max_length=50, null=False, default='', verbose_name=u'Примечание')
    dt=models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.name


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    timestamp = models.DateField(auto_now_add=True, auto_now=False)

@receiver(post_save, sender = equipment)
def add_history(instance, **kwargs):
    a_record=history()
    a_record.id_eq=instance.objects.get()
    a_record.type=instance.type
    a_record.name=equipment.name
    a_record.ter=equipment.ter
    a_record.dep=equipment.dep
    a_record.bild=equipment.bild
    a_record.status = equipment.status
    a_record.note=equipment.note
    a_record.dt=datetime.now
    a_record.save()