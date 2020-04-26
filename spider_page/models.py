from django.db import models

from django.db import models

# Create your models here.

class longyitjzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    cj = models.CharField(max_length=40)
    gg = models.CharField(max_length=20)
    xq = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    price2 = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'longyi_tjzq_01'

class rjyiyaoxpsj(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    cj = models.CharField(max_length=40)
    gg = models.CharField(max_length=20)
    xq = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'rjyiyao_xpsj'

class scjrmzszq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    cj = models.CharField(max_length=40)
    price = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'scjrm_zszq'