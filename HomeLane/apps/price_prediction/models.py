from django.db import models

# Create your models here.

class HomeLane(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.word)

    def __repr__(self):
        return '{}'.format(self.word)

    class Meta:
        db_table = 'homelane'
        verbose_name = 'HomeLane'
