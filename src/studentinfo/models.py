from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class StudentInfo(models.Model):
	first_name = models.CharField(max_length=20, null=False, blank=False)
	last_name = models.CharField(max_length=20, null=False, blank=False)
	email = models.EmailField()
	Math_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	English_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	Science_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	Social_Studies_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	Health_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	Chemistry_101 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	English_201 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	Math_201 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

	def __unicode__(self):
		return smart_unicode(self.first_name+" "+self.last_name)