from django.db import models

# Create your models here.
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return 'CrudUser {}'.format(self.id)

class t_staff(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True)
	position = models.CharField(max_length=30)
	status = models.CharField(max_length=30, default='Active')
	user = models.IntegerField(default=1, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return 't_staff {}'.format(self.id)

class t_calls(models.Model):
	rootid = models.ForeignKey(t_staff, on_delete=models.CASCADE)
	trip_no = models.CharField(max_length=10, blank=True, null=True)
	driver = models.CharField(max_length=30, blank=True)
	notes = models.CharField(max_length=100, blank=True)
	private_notes = models.CharField(max_length=100, blank=True, null=True)
	user = models.IntegerField(default=1, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return 't_calls {}'.format(self.id)


class t_dict(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	category = models.CharField(max_length=30)
	status = models.CharField(max_length=30, default='Active')
	user = models.IntegerField(default=1, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return 't_dict {}'.format(self.id)		