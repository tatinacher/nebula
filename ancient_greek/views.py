from rest_framework import viewsets

from .serializers import CharacterSerializer
from .models import Character

class CharacterModelViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)