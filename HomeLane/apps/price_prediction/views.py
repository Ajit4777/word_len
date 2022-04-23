from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomeLane
from .serializers import WordSerializer
# Create your views here.
import itertools


class WordGet(APIView):

    def get(self, request, **kwargs):
        word1 = kwargs.get('word1', None)
        word2 = kwargs.get('word2', None)
        test_str = word1+word2
        words = HomeLane.objects.all()
        c_words = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1) \
                   if len(test_str[i:j]) > 3]
        queryset = words.filter(word__gt=3, word__in=c_words)
        serializer = WordSerializer(queryset, many=True)
        return Response(serializer.data)
