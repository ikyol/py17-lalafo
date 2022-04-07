from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = AdvertisementGallery
        fields = ['picture']


# class CreateAdvertisementSerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         write_only=True, child=serializers.ImageField()
#     )


#     class Meta:
#         model = Advertisement
#         # fields = '__all__'
#         exclude = ['author']

#     def create(self, validated_data):
#         validated_data['author'] = self.context['request'].user
#         images = validated_data.pop('images', [])
#         ads = super().create(validated_data)
#         for picture in images:
#             AdvertisementGallery.objects.create(advertisement=ads, picture=picture)
#         return ads


class AdvertisementListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'city', 'price', 'image']

    def get_image(self, advertisement):
        first_image_obj = advertisement.images.first()
        if first_image_obj is not None:
            return first_image_obj.picture.url
        return ''


# class AdvertisementDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advertisement
#         fields = '__all__'

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['images'] = ImageSerializer(instance.images.all(), many=True).data
#         return representation

# class UpdateAdvertisementSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Advertisement
#         fields = ['title', 'text', 'city', 'price']


class AdvertisementSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True, child=serializers.ImageField()
    )
    class Meta:
        model = Advertisement
        # fields = "__all__"
        exclude = ['author']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        images = validated_data.pop('images', [])
        ads = super().create(validated_data)
        for picture in images:
            AdvertisementGallery.objects.create(advertisement=ads, picture=picture)
        return ads

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        return representation