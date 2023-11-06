from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from . models import UserInfo,Services,Skills,Education,Portfolio,Cuntuct_us,Experience
from . mixins import TranslatedSerializerMixin

class UserInfoSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = UserInfo)
    class Meta:
        model = UserInfo
        fields = '__all__'
    def to_representation(self, instance):
        obj = super().to_representation(instance)
        obj['projects'] = instance.projects
        return obj

class ServiceSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Services)
    class Meta:
        model = Services
        exclude = ['user']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ['user']

class EducationSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Education)
    class Meta:
        model = Education
        exclude = ['user']

class PortfolioSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Portfolio)
    class Meta:
        model = Portfolio
        exclude = ['user']

class CuntuctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuntuct_us
        fields = "__all__"

class ExperienceSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Experience)
    class Meta:
        model = Experience
        exclude = ['user']