from django.shortcuts import render
from django.http import Http404
from .models import Question, Choice

# Create your views here.

def index(request):
	return render(request, 'index.html', {'questions': Question.objects.all()})


def exibir_question(request, question_id):
	try:
		question_procurada = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question não existe")
	return render(request, 'question.html', {'question': question_procurada})

