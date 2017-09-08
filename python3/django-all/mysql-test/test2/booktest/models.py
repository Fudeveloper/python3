from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(is_delete=False)

    def create(clsb, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcoment = 0
        b.is_delete = False
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcoment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()

    def __str__(self):
        return self.btitle



class HeroInfo(models.Model):
    hname =  models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=40)
    hbook = models.ForeignKey(BookInfo)
