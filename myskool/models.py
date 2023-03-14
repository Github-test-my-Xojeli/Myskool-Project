from django.db import models

# Create your models here.

class MySkool(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Age = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Class_name = models.CharField(max_length=255)
    Monday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Tuesday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Wensday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Thursday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Friday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Saturday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Sunday = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Weekly = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Monthly = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    Yearly = models.PositiveBigIntegerField(default=0, null=True, blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = 'MySkool'
        verbose_name_plural = 'MySkool'

    def __str__(self):
        return self.first_name

    def skool_week(self):
        return self.Monday + self.Tuesday + self.Wensday + self.Thursday + self.Friday + self.Saturday + self.Sunday
    
    def skool_mon(self):
        return self.skool_week
        
    def skool_year(self):
        return self.skool_week