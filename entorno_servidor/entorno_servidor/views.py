from django.shortcuts import render
def homepage(request):
 
 request.session['visitas'] = request.session.get('visitas', 0) + 1
 
 return render(request, 'home.html')
