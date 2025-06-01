from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Ad,Category
from .forms import AdCreateForm


class AdCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ad
    form_class = AdCreateForm
    template_name = 'ads/ad_create.html'
    success_message = "Объявление успешно создано!"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})

def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

def ad_create(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_create.html', {'ads': ads})

# Create your views here.
class AdCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ad
    form_class = AdCreateForm
    template_name = 'ads/ad_create.html'
    success_message = "Объявление успешно создано!"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if Category.objects.exists():
            context['popular_categories'] = Category.objects.annotate(
                num_ads=Count('ad')
            ).order_by('-num_ads', '-id')[:5]
        else:
            default_categories = [
                "Электроника",
                "Одежда",
                "Недвижимость",
                "Транспорт",
                "Услуги"
            ]
            for name in default_categories:
                Category.objects.get_or_create(name=name)

            context['popular_categories'] = Category.objects.order_by('-id')[:5]

        return context