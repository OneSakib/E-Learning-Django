from django.contrib import admin
from .models import Subject, Course, Module, Content, ItemBase, Text, Video, Image, File


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


admin.site.register(Content)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Video)
