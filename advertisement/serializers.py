from distutils.command.build_scripts import first_line_re
from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = AdvertisementGallery
        fields = ['picture']


class CreateAdvertisementSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True, child=serializers.ImageField()
    )


    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        ads = super().create(validated_data)
        for picture in images:
            AdvertisementGallery.objects.create(advertisement=ads, picture=picture)
        return ads


class AdvertisementListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'city', 'price', 'image']

    def get_image(self, advertisement):
        first_image_obj = advertisement.imgaes.first()
        if first_image_obj is not None:
            return first_image_obj.picture.url
        return ''