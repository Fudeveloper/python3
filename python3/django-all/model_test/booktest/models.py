from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcoment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle
    class Meta:
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=40)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname

    def show_book(self):
        return self.hbook