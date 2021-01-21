from django.contrib import admin
from .models import Blog,Category
# from tinymce.models import HTMLField
# from tinymce.widgets import TinyMCE
# from mce_filebrowser.admin import MCEFilebrowserAdmin

# class BlogAdmin(MCEFilebrowserAdmin):
#     list_display = ('title', 'category', 'view_count')
#     formfield_overrides = {
#         HTMLField: {'widget':TinyMCE(attrs={'row':40, 'cols':125})}
#     }

admin.site.register(Blog)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'count_post')

#     class Meta:
#         model = Category

admin.site.register(Category)
