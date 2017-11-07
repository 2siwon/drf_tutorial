from rest_framework import viewsets, permissions

from ..permissions import IsOwnerOrReadOnly
from ..models import Snippet
from ..serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    serializer_class = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
