from django.shortcuts import render

# Create your views here.

def bs_comp(request):
    return render(request,'bs_comp.html')

def bs_alerts(request):
    return render(request,'bs_alerts.html')

def bs_badges(request):
    return render(request,'bs_badges.html')

def bs_breadcrumb(request):
    return render(request,'bs_breadcrumb.html')

def bs_buttons(request):
    return render(request,'bs_buttons.html')

def bs_cards(request):
    return render(request,'bs_cards.html')

def bs_carousel(request):
    return render(request,'bs_carousel.html')

def bs_forms(request):
    return render(request,'bs_forms.html')

def bs_carousel_download(request):
    return render(request,'bs_carousel_download.html')

def bs_inputgrp(request):
    return render(request,'bs_inputgrp.html')



