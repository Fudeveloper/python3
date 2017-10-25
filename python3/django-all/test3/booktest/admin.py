from django.contrib import admin

# Register your models here.


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display=[
        'btitle',
        'bpub_date'
    ]

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = [
        'hname'
    ]
# admin.site.register(BookInfo)

@admin.register(AreaInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = [
        'title',

    ]