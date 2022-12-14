from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'context', 'created_time', 'last_modified', 'visible', 'important', 'created_user']

class NoticeCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['visible', 'important']