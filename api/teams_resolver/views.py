from rest_framework import permissions, viewsets

from .models import Teammate, Team
from .serializers import TeammateSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permissions_classes = [permissions.IsAuthenticated]


class TeammateViewSet(viewsets.ModelViewSet):
    queryset = Teammate.objects.all()
    serializer_class = TeammateSerializer
    permissions_classes = [permissions.IsAuthenticated]
