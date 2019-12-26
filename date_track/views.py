from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    current_user = "Meet"
    return render(request, 'home.html',
                {'date':datetime.now().year,'login':current_user})