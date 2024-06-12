from django.contrib import admin
from database.models import Profile,UserModel,add_expense

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display=('name','category','date','amount','type')
    

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','image','location','contact')
    



admin.site.register(add_expense,ExpenseAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserModel)