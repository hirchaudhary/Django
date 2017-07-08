from django.shortcuts import render

def index(request):
	return render(request, 'portfolio_me/index.html')

def test(request):
	return render(request, 'portfolio_me/testimonial.html')
