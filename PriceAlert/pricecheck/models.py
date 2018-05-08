from django.db import models

# Create your models here.

class Alert(models.Model):
	source = models.CharField(max_length=250)
	item = models.CharField(max_length=100, default="")
	url = models.URLField(default="")
	product_name = models.CharField(max_length=250)
	alert_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	email_id = models.EmailField(max_length=70,blank=False)

	def __str__(self):
		return self.source + " --- " + self.product_name + " --- " + self.email_id 