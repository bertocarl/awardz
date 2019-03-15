from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="", blank="")
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')
    bio = models.TextField(blank="", default="")
    phonenumber = models.IntegerField(max_length=140, blank="",default="")

    def __str__(self):
        return f'{self.user.username} Profile'
