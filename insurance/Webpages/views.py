from django.shortcuts import render
from .forms import BmiForm, BmiMeasurementForm, WthForm, WthMeasurementForm
from .models import Bmi, Wth
# Create your views here.
def index(request):
	return render(request,'temp/index.html',{})

def location(request):
	return render(request,'temp/location.html',{})

def faq(request):
    return render(request,'temp/faq.html',{})

def insurance(request):
    return render(request,'temp/insurance.html',{})

def homeinsurance(request):
    return render(request,'temp/homeinsurance.html',{})

def bmi(request):
    if request.method == "POST":
        form = BmiMeasurementForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = weight/height*2
            return render(request, "temp/bmi.html", {"form": form, "bmi": bmi})
    else:
        measurements = Bmi.objects.all()
        form = BmiMeasurementForm()
    return render(request, "temp/bmi.html", {"form": form, "measurements": measurements})

def wthratio(request):
    if request.method == "POST":
        form = WthMeasurementForm(request.POST)
        if form.is_valid():
            waist = form.cleaned_data["waist"]
            hip = form.cleaned_data["hip"]
            wthratio = waist/hip
            return render(request, "temp/wthratio.html", {"form": form, "wthratio": wthratio})
    else:
        measurements = Wth.objects.all()
        form = WthMeasurementForm()
    return render(request, "temp/wthratio.html", {"form": form, "measurements": measurements})    