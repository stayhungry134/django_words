"""
name: serializers
create_time: 2023/5/17
author: Ethan

Description: 
"""
from rest_framework import serializers

from base.serializers import BaseModelSerializer
from word.models import NewWord, ReviewRecord


class NewWordSerializer(BaseModelSerializer):
    class Meta:
        model = NewWord
        fields = ('id', 'word', 'meaning', 'collins', 'uk_audio', 'uk_phone', 'us_audio', 'us_phone')
        content_type = 'application/json'


class ReviewRecordSerializer(serializers.ModelSerializer):
    word = NewWordSerializer()

    class Meta:
        model = ReviewRecord
        fields = ('id', 'word', 'last_review', 'next_review', 'familiarity', 'review_times')
        content_type = 'application/json'
