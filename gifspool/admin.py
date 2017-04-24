from django.contrib import admin

from .models import Gif, Category, Like

class GifAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator','name', 'tags', 'post_to', 'upload_date')
    fields = ('creator', 'category', 'name', 'tags', 'post_to', 'shocked', 'loved', 'laugh', 'gif_file')
    # readonly_fields 
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','num_gifs', 'num_likes')

class LikeAdmin(admin.ModelAdmin):
	list_display = ('id', 'gif_id','user_id', 'shocked', 'loved', 'laugh')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Gif,  GifAdmin)
admin.site.register(Like,  LikeAdmin)