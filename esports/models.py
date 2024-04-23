from django.db import models
from django.utils.timezone import now

class Lol(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    spread1 = models.CharField(max_length=64)
    spread2 = models.CharField(max_length=64)
    win1 = models.CharField(max_length=64)
    win2 = models.CharField(max_length=64)
    total1 = models.CharField(max_length=64)
    total2 = models.CharField(max_length=64)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.team1 + ' VS ' + self.team2
    
    def spreads(self):
        return self.spread1 + ' And ' + self.spread2
    
    
    def testing():
        return "hello!"
        

class LolWin(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    win1_decimal = models.FloatField(max_length=64)
    win2_decimal = models.FloatField(max_length=64)
    win1_probability = models.IntegerField()
    win2_probability = models.IntegerField()
    win1_ev = models.FloatField(max_length=64)
    win2_ev = models.FloatField(max_length=64)
    win1_site = models.CharField(max_length=64)
    win2_site = models.CharField(max_length=64)
    date = models.CharField(max_length=64)


class LolSpread(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    spread1_decimal = models.FloatField(max_length=64)
    spread2_decimal = models.FloatField(max_length=64)
    spread1_ou = models.FloatField(max_length=16)
    spread2_ou = models.FloatField(max_length=16)
    spread1_probability = models.IntegerField()
    spread2_probability = models.IntegerField()
    spread1_ev = models.FloatField(max_length=64)
    spread2_ev = models.FloatField(max_length=64)
    spread1_site = models.CharField(max_length=64)
    spread2_site = models.CharField(max_length=64)
    date = models.CharField(max_length=64)


class LolTotal(models.Model):
    team1 = models.CharField(max_length=64)
    team2 = models.CharField(max_length=64)
    total1_decimal = models.FloatField(max_length=64)
    total2_decimal = models.FloatField(max_length=64)
    total_over = models.FloatField(max_length=16)
    total_under = models.FloatField(max_length=16)
    total1_probability = models.IntegerField()
    total2_probability = models.IntegerField()
    total1_ev = models.FloatField(max_length=64)
    total2_ev = models.FloatField(max_length=64)
    total1_site = models.CharField(max_length=64)
    total2_site = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
