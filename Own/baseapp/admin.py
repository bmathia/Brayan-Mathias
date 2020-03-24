from django.contrib import admin
from django.core.files.base import ContentFile
from PIL import Image
from baseapp.models import Pictures, Profile_pic,Post,Notices,Lectors,News

# Register your models here.

admin.site.register(Pictures)
admin.site.register(Profile_pic)
admin.site.register(Post)
admin.site.register(Notices)
admin.site.register(Lectors)
admin.site.register(News)
