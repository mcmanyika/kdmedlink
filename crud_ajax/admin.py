from django.contrib import admin
from .models import CrudUser, t_calls, t_acct, t_dict

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'name', 'address']
	class Meta:
		model = CrudUser
admin.site.register(CrudUser, UserAdmin)

admin.site.register(t_acct)
admin.site.register(t_calls)
admin.site.register(t_dict)