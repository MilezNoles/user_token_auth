from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ("id", "username", "email", "password", "is_superuser", "is_active", "last_login")
        read_only_fields = ('last_login',)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.password = make_password(user.password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop("password", ""))
        return super().update(instance, validated_data)
