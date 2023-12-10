from django.db import models

# Create your models here.

class DriverInformation(models.Model):
    driverName = models.CharField(max_length=200)
    numberOfDrowsiness = models.CharField(max_length=200)
    numberOfPhoneUsage = models.CharField(max_length=200)
    numberOfWorkingDay = models.IntegerField(default = 0)
    numberOfRuleViolation = models.CharField(max_length=200)
    numberOfTrafficViolation = models.IntegerField(default = 0)
    drivingLicenseExpiredDate = models.DateTimeField(default=0)
    firstLogInTime = models.DateTimeField(default = 0)
    lastOnlineTime = models.DateTimeField(default = 0)
    drivingDuration = models.IntegerField(default = 0)
    def __str__(self):
        return self.driverName