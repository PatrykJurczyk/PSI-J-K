from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Gra, Gatunek, Uzytkownik, Producent
from .serializers import GraSerializer, GatunekSerializer, UzytkownikSerializer, ProducentSerializer
from django.views.generic import TemplateView, CreateView, UpdateView, FormView, ListView, DeleteView
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from PSIGameLibrary.settings import LOGIN_REDIRECT_URL
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse


class LandingPage(TemplateView):
    template_name = 'landing_page.html'

class LogoutView(LogoutView):
    template_name = 'logout.html'

class LoginView(LoginView):
    template_name = 'login.html'
    def get_default_redirect_url(self):
        return resolve_url(self.next_page or LOGIN_REDIRECT_URL)

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Uzytkownik
    fields = [
        'first_name',
        'last_name',
        'email',
        'address',
        'phone_number',
    ]
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile_update')

    def get_object(self):
        return self.request.user


class ProducerListView(ListView):
    paginate_by = 5
    model = Producent
    template_name = 'producers_list.html'
    queryset = Producent.objects.all()

class GamesListView(ListView):
    paginate_by = 5
    template_name = 'gameslist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producent'] = Producent.objects.get(id=self.kwargs['id'])
        return context

    def get_queryset(self):
        id = self.kwargs['id']
        return Producent.objects.get(id=id).gra_set.all()


class GameList(APIView):
    def get(self, request, format=None):
        gra = Gra.objects.all()
        serializer = GraSerializer(gra, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetails(APIView):
    def get_obiect(self, pk):
        try:
            return Gra.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        serializer = GraSerializer(gra)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        serializer = GraSerializer(gra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        gra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GanreList(APIView):
    def get(self, request, format=None):
        gatunek = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunek, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GatunekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        uzytkownik = Uzytkownik.objects.all()
        serializer = UzytkownikSerializer(uzytkownik, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UzytkownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerList(APIView):
    def get(self, request, format=None):
        producent = Producent.objects.all()
        serializer = ProducentSerializer(producent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProducentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required()
def cart_add(request, id):
    if request.method == "POST":
        cart = Cart(request)
        product = Gra.objects.get(id=id)
        cart.add(product=product)
        return JsonResponse({'status': 'Dodano do koszyka'})
    return JsonResponse({'status': 'error'})

@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Gra.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Gra.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Gra.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart.html')


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

