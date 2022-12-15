from rest_framework import serializers
from applications.users.models import User #TODO 3 registro usuarios


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')
     
	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance