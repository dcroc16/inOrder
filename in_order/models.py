from django.db import models

# Create your models here.
class OrderTitle(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=300)
	items = models.ManyToManyField('OrderListItem')

	def get_tab_data(self, filePath):
		self.f = open(filePath, 'r')
		self.splitF = []
		self.cleanI = ''
		for i in self.f.readlines():
			self.cleanI = i.replace('\n', '')
			self.splitF.append(self.cleanI.split('\t'))
		self.f.close()
		for i in self.splitF:
			self.a = OrderListItem(
					item=i[0],
					position=int(i[1]),
					oID=self,
					completed=False)
			self.a.save()
		print "Completed"

	def __unicode__(self):
		return self.title

class OrderListItem(models.Model):
	id = models.AutoField(primary_key=True)
	oID = models.ForeignKey('OrderTitle')
	position = models.IntegerField()
	item = models.CharField(max_length=300)
	completed = models.BooleanField()



	def __unicode__(self):
		return self.item

	def print_all(self):
		for i in self.objects.all():
			print self.id
			print self.oID
			print self.position
			print item

