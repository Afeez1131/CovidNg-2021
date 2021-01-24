from rest_framework import serializers
from .models import Total
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TotalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total
		fields = ('day', 'confirmed', 'death', 'discharged')
		# extra_kwargs = {'url': {'lookup_field': 'day'}}

class Serializer(serializers.ModelSerializer):
	class Meta:
		model = Total
		fields = ('day', 'confirmed', 'death', 'discharged')

class TotalViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('__all__')

