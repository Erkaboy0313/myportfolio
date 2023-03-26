from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from . models import UserInfo
from . mixins import TranslatedSerializerMixin

class UserInfoSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = UserInfo)
    class Meta:
        model = UserInfo
        fields = '__all__'