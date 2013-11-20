from django.contrib import admin


class SlugMixin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

