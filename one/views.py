from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse('hello index')


def show(request, show_str):
	context = {
		'show_str': show_str
	}
	return render(request, 'one/show.html', context)
