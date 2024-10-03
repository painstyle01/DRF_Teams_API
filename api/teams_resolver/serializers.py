from .models import Teammate, Team
from rest_framework import serializers


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "team_name"]


class TeammateSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.SlugRelatedField(
        many=False,
        slug_field="id",
        queryset = Team.objects.all(),
    )

    class Meta:
        model = Teammate
        fields = ["id", "first_name", "last_name", "email", "team"]

