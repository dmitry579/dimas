from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Ad, Category

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})

def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

# Create your views here.
