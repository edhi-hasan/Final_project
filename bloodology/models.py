from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime,random
from tinymce.models import HTMLField

# Create your models here.

class UserProfile(models.Model):
        BLOOD_GROUP_CHOICES = [
                ('A+', 'A+'),
                ('A-', 'A-'),
                ('B+', 'B+'),
                ('B-', 'B-'),
                ('O+', 'O+'),
                ('O-', 'O-'),
                ('AB+', 'AB+'),
                ('AB-', 'AB-'),
        ]
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=150)
        blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=5)
        phone_number = models.CharField(max_length=15)
        address = models.CharField(max_length=250)
        profile_img = models.ImageField(upload_to='Images')
        otp = models.CharField(max_length=6, blank=True, null=True)  # Store OTP
        otp_expiration = models.DateTimeField(blank=True, null=True)  # Expiration time for OTP
        last_blood_donation = models.DateTimeField(blank=True, null=True)  # Last blood donation date

        def __str__(self):
                return self.name

        def generate_otp(self):
        # Generate a 6-digit OTP
                otp = str(random.randint(100000, 999999))
                self.otp = otp
                self.otp_expiration = timezone.now() + datetime.timedelta(minutes=5)  # Set expiration time for OTP
                self.save()
                return otp
        # Add method to check if available
        def is_available(self):
                if self.last_blood_donation:
                        return timezone.now() > self.last_blood_donation + datetime.timedelta(days=90)
                return False

        # Add method to calculate days remaining
        def days_remaining(self):
                if self.last_blood_donation:
                        days_passed = (timezone.now() - self.last_blood_donation).days
                        return max(0, 90 - days_passed)
                return 90  # If no donation date is set, show 90 days
        
class BlogPost(models.Model):
        user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        content = HTMLField() 
        blogPostTime = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.title
        

class BloodRequestPost(models.Model):
        BLOOD_GROUP_CHOICES = [
                ('A+', 'A+'),
                ('A-', 'A-'),
                ('B+', 'B+'),
                ('B-', 'B-'),
                ('O+', 'O+'),
                ('O-', 'O-'),
                ('AB+', 'AB+'),
                ('AB-', 'AB-'),
        ]
        user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
        date_time = models.DateTimeField()
        Disease_name = models.CharField(max_length=100)
        No_of_bag = models.PositiveIntegerField()
        medical_name = models.CharField( max_length=150)
        location = models.CharField(max_length=255)
        phone_number = models.CharField(max_length=15)
        created_at = models.DateTimeField(auto_now_add=True)