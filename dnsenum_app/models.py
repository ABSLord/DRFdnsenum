""" Models for `dnsenum` utility """ 

from uuid import uuid4

from django.db import models


class ProcessManager(models.Manager):
    """ Django manager for `dnsenum` utility process """

    def insert(self):
        """ Simple create a new record in database and return item ID """
        item = self.create()
        return item.id


class Process(models.Model):
    """ Model for `dnsenum` utility process """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    output = models.TextField(
        verbose_name='Result of the utility running',
        default='',
        blank=True,
        null=False
    )
    ready = models.BooleanField(
        verbose_name='Flag for the utility readiness (False - running, True - done)',
        default=False,
        blank=False,
        null=False
    )
    exitcode = models.IntegerField(
        verbose_name='Exit code of utility process',
        default=None,
        blank=False,
        null=True
    )

    objects = ProcessManager()

    def ready(self, exitcode=0, output=''):
        """ Set process status is ready, set process output and exitcode """
        self.ready = True
        self.output = output
        self.exitcode = exitcode
        self.save()
