from rest_framework import serializers
from applications.users.models import User, Titulacion


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'first_name',
   			'last_name',
			'nif',
			'email_institucional',
			'email_personal',
			'telefono',
			'titulacion',
			'curso',
			'password',
			'tipo'
		)
     
	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance


class UserTitulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulacion
        fields = (
            'id',
			'titulo',
			'descripcion',
			'duracion'
		)