from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'main_website/home.html')
def represent(request):
	return render(request,'main_website/represent.html')