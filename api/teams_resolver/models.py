from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.team_name}"


class Teammate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True) # To keep users connected to teams

    def __str__(self):
        return f"{self.first_name} '{self.email}' {self.last_name}"