from django.shortcuts import render

# Create your views here.
from django.views import View

from chomik.models import Sala


class IndexView(View):
    def get(self, request):
        salki = Sala.objects.all()
        ctx = dict(
            salki=salki
        )
        return render(request, 'chomik/main.html', context=ctx)

class RoomNewView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class RoomModifyView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class RoomDeleteView(View):
    def get(self, request):
        pass


class RoomView(View):
    def get(self, request):
        pass
