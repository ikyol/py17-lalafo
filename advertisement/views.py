from dataclasses import field
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from advertisement.permissions import IsAuthor
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

# class CreateAdvertisementView(CreateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = CreateAdvertisementSerializer
#     permission_classes = [IsAuthenticated]

# class AdvertisementsListView(ListAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementListSerializer


# class AdvertisementDetailsView(RetrieveAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementDetailSerializer

# class UpdateAdvertisementView(UpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = UpdateAdvertisementSerializer
#     permission_classes = [IsAuthor]

#     def get_serializer_context(self):
#         return {'request': self.request}

# class DeleteAdvertisementView(DestroyAPIView):
#     queryset = Advertisement.objects.all()
#     permission_class = [IsAuthor]


class AdvertisementFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Advertisement
        fields = ['category', 'city']


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'text', 'city']
    ordering_fields = ['price', 'title']
    filterset_class = AdvertisementFilter

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = AdvertisementListSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return []


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []