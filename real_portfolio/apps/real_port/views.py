from django.shortcuts import render

def index(request):
	return render(request, 'real_port/index.html')

def test(request):
	return render(request, 'real_port/testimonial.html')

def about(request):
	return render(request, 'real_port/about.html')

def project(request):
	return render(request, 'real_port/project.html')
