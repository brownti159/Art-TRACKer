from rest_framework import serializers
from places.models import Work


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'title', 'year', 'latitude', 'longitude', 'category', 'description', 'photo', 'notes', 'wheelchairAccessible']

# class WorkSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=200)
#     # creators = serializers.CharField(required=False, blank=True, null=True)
#     year = serializers.IntegerField(required=False, allow_null=True)
#     latitude = serializers.DecimalField(required=False, allow_null=True, max_digits=9, decimal_places=6)
#     longitude = serializers.DecimalField(required=False, allow_null=True, max_digits=9, decimal_places=6)
#     category = serializers.CharField(max_length=20, allow_blank=True, allow_null=True)
#     description = serializers.CharField(style={'base_template': 'textarea.html'}, allow_blank=True, allow_null=True)
#     photo = serializers.ImageField(required=False, allow_null=True)
#     notes = serializers.CharField(style={'base_template': 'textarea.html'}, allow_blank=True, allow_null=True)
#     wheelchairAccessible = serializers.BooleanField(required=False, allow_null=True)

    
    # def create(self, validated_data):
    #     return Work.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     # instance.creators = validated_data.get('creators', instance.creators)
    #     instance.year = validated_data.get('year', instance.year)
    #     instance.latitude = validated_data.get('latitude', instance.latitude)
    #     instance.longitude = validated_data.get('longitude', instance.longitude)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.photo = validated_data.get('photo', instance.photo)
    #     instance.notes = validated_data.get('notes', instance.notes)
    #     instance.wheelchairAccessible = validated_data.get('wheelchairAccessible', instance.wheelchairAccessible)
    #     instance.save()
    #     return instance