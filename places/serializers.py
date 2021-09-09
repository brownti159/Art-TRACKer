from rest_framework import serializers
from places.models import Artist, Work



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'website']



class WorkSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    class Meta:
        model = Work
        fields = ['id', 'title', 'artists', 'year', 'latitude', 'longitude', 'category', 'description', 'photo', 'notes', 'wheelchairAccessible']

