from django.contrib import admin
from .models import Project, Person, Opportunity, Skill

# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
    # fields = [f.name for f in Person._meta.get_fields()]
    # list_display = [f.name for f in Person._meta.get_fields()]
    #
    # def image_img(self):
    #     if self.image:
    #         return u'<img src="%s" />' % self.image.url
    #     else:
    #         return '(No image found)'
    #     image_img.short_description = 'Thumb'
    #     image_img.allow_tags = True

[admin.site.register(c) for c in [Project, Person, Opportunity, Skill]]

# admin.site.register(Person, PersonAdmin)
