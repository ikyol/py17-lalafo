from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class CreateAdvertisementView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = CreateAdvertisementSerializer
    permission_classes = [IsAuthenticated]

class AdvertisementsListView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer


class AdvertisementDetailsView(RetrieveAPIView):
    pass

class UpdateAdvertisementView(UpdateAPIView):
    pass

class DeleteAdvertisementView(DestroyAPIView):
    queryset = Advertisement.objects.all()