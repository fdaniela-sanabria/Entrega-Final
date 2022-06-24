from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from reviews.models import ReviewsModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm



class ReviewsList(ListView):

    model = ReviewsModel
    template_name = "reviews/reviews_list.html"


class ReviewsDetail(DetailView):

    model = ReviewsModel
    template_name = "reviews/reviews_detail.html"


class ReviewCreate(LoginRequiredMixin, CreateView):

    model = ReviewsModel
    success_url = reverse_lazy("reviews_list")
    fields = ["titulo", "director", "estreno", "cuerpo"]
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = ReviewsModel
    success_url = reverse_lazy("reviews_list")
    fields = ["titulo", "director", "estreno", "cuerpo"]

    def test_func(self):
        exist = ReviewsModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class ReviewDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = ReviewsModel
    success_url = reverse_lazy("reviews_list")

    def test_func(self):
        exist = ReviewsModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False



def reviews_inicio(request):
    return render(request, 'reviews/reviews_inicio.html')

def about_us(request):
    return render(request, 'reviews/about_us.html')


class ReviewsLogin(LoginView):
    template_name = 'reviews/reviews_login.html'
    next_page = reverse_lazy("reviews_list")

class ReviewsLogout(LogoutView):
    template_name = 'reviews/reviews_logout.html'