from django.shortcuts import render
from .models import Results_model

# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    marks_obj = Results_model.objects.all()  # ORM Query # Query set
    my_dict = {'marks_obj': marks_obj}
    return render(request, 'about.html', context=my_dict)