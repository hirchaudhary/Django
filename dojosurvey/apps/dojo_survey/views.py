from django.shortcuts import render, redirect

def index(request):
    return render(request, 'dojo_survey/index.html')

def survey(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        language = request.POST['language']
        description = request.POST['description']
        validation = True
        if len(name) < 1:
            validation = False
        if len(description) < 5:
            validation = False
        if validation:
            request.session['count']       += 1
            request.session['name']        = name
            request.session['location']    = location
            request.session['language']    = language
            request.session['description'] = description
            return redirect('/result')
        return redirect('/')
    else:
        return redirect('/')

def result(request):
    return render(request, 'dojo_survey/result.html')
