from django.contrib import admin
from app.models import Contact
from app.models import Team
from app.models import Admin
from app.models import Frontadmin
from app.models import Portfolio
from app.models import Service
from app.models import Blog
from app.models import Testomonial
# Register your models here.
class Contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone','message','subject','date',)


class Adminadmin(admin.ModelAdmin):
    list_display=('name','title','date',)

class Teamadmin(admin.ModelAdmin):
    list_display=('name','title','date',)

class Frontadminadmin(admin.ModelAdmin):
    list_display=('name','title','date',)

class Portfolioadmin(admin.ModelAdmin):
    list_display=('title','description','date',)

class Serviceadmin(admin.ModelAdmin):
    list_display=('title','description','date',)

class Blogadmin(admin.ModelAdmin):
    list_display=('title','description','date',)

class Testomonialadmin(admin.ModelAdmin):
    list_display=('name','title','description','date',)



admin.site.register(Contact,Contactadmin)
admin.site.register(Team,Teamadmin)
admin.site.register(Admin,Adminadmin)
admin.site.register(Frontadmin,Frontadminadmin)
admin.site.register(Portfolio,Portfolioadmin)
admin.site.register(Service,Serviceadmin)
admin.site.register(Blog,Blogadmin)
admin.site.register(Testomonial,Testomonialadmin)