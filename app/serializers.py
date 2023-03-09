from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from . models import Post, UserInfo
from . mixins import TranslatedSerializerMixin

class PostSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Post)
    class Meta:
        model = Post
        fields = ('translations', 'author', 'created_on', 'updated_on')

class UserInfoSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = UserInfo)
    class Meta:
        model = UserInfo
        fields = '__all__'