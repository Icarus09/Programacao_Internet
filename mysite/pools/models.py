from django.db import models
# Create your models here.
 
class Question(models.Model):
	question_text = models.CharField(max_length=100, null=False)
	closed = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=False)

	def __str__(self):
		return '%s' % (self.question_text)

class Choice(models.Model):
	choice_text = models.CharField(max_length=100)
	votes = models.IntegerField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True, related_name='choices')

	def __str__(self):
		return '%s' % (self.choice_text)
