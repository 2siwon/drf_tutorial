from rest_framework import generics

from ..models import Snippet
from ..serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    query = Snippet.objects.all()
    serializer_class = SnippetSerializer