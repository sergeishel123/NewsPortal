from django.contrib import admin
from .models import Post,Author,Usersubscriberscategory,PostCategory,Category
from modeltranslation.admin import TranslationAdmin
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Usersubscriberscategory)
admin.site.register(PostCategory)
admin.site.register(Category)
# Register your models here.

class Post_Admin(admin.ModelAdmin):
    list_display = (
    )

class PostAdmin(TranslationAdmin):
    model = Post