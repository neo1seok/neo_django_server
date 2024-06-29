

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Password,PasswordHeader
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class PasswordHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordHeader
        fields = ('id','title')
class PasswordHeaderDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordHeader
        fields = ('id','title', 'hint','special_letter','etc')

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    pheader_id = PrimaryKeyRelatedField(read_only=True,source="pheader")#ForeignKey 의 id로 표시 한다.
    #pheader = PasswordHeaderSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.
    pheader_title = serializers.SerializerMethodField()
    class Meta:
        model = Password
        fields = ('id','pheader_id', 'pheader_title','site','ptail')

    def get_pheader_title(self, obj):
        return obj.pheader.title

class PasswordCreateSerializer(serializers.ModelSerializer):
    pheader_id = serializers.SerializerMethodField()
    pheader_title = serializers.SerializerMethodField()
    #pheader = PasswordHeaderDetailSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.

    class Meta:
        model = Password
        fields = ('id','pheader_id','pheader_title', 'site','ptail','site_id')

    def get_pheader_id(self, obj):
        return obj.pheader.id

    def get_pheader_title(self, obj):
        return obj.pheader.title

class PasswordDetailSerializer(serializers.ModelSerializer):
    pheader_id = PrimaryKeyRelatedField(queryset=PasswordHeader.objects.all(), source="pheader")  # ForeignKey 의 id로 표시 한다.
    #pheader_id = serializers.SerializerMethodField()
    pheader_title = serializers.SerializerMethodField()
    #pheader = PasswordHeaderDetailSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.

    class Meta:
        model = Password
        fields = ('id','pheader_id', 'pheader_title','site','ptail','site_id','etc','status','comment')

    # def get_pheader_id(self, obj):
    #     return obj.pheader.id

    def get_pheader_title(self, obj):
        return obj.pheader.title
    # @swagger_auto_schema(
    #     operation_description="Create a new book",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['title', 'author_id'],
    #         properties={
    #             'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the book'),
    #             'author_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the author'),
    #         },
    #         example={
    #             'title': 'New Book',
    #             'author_id': 1,
    #         }
    #     ),
    #     responses={201: 'Created'}
    # )
    # def create(self, validated_data):
    #     return super().create(validated_data)