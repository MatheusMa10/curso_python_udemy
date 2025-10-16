from django.shortcuts import render

# from django.shortcuts import render
# Create your views here.

def home(request):
    print('Home')

    context = {
        'text': 'Estamos no home',
        'title': 'Home - ',
    }
    
    return render(
        request,
        'home/index.html',
        context
    )