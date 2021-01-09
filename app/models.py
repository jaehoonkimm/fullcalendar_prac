from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CalendarEvent(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    groupId = models.CharField(_('GroupId'), max_length=100, default=False)

    def __str__(self):
        return self.title