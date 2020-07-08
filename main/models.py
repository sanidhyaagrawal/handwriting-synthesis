from django.db import models



class template(models.Model):
	username  = models.CharField(max_length=100)
	template1 = models.FileField(upload_to= 'templates/')
	template2 = models.FileField(upload_to= 'templates/')
	template3 = models.FileField(upload_to= 'templates/')
	font_width = models.SmallIntegerField()
	
		
	def delete(self, *args, **kwargs):
		self.template1.delete()
		self.template2.delete()
		self.template3.delete()
		super().delete(*args, **kwargs)
