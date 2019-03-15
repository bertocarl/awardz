from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="", blank="")
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')
    bio = models.TextField(blank="", default="")
    phonenumber = models.IntegerField(max_length=140, blank="",default="")

    def __str__(self):
        return f'{self.user.username} Profile'

class Image(models.Model):
   """
   This is the class we will use to create images of the projects
   """
   image_url = models.ImageField(upload_to = "images/")
   name = models.CharField(max_length = 30)
   description = models.TextField()
   category = models.ForeignKey(Category)



   def save_image(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

   def delete_image(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()

   def update_image(self,val):
       """
       This is the method to update the instance
       """
       Image.objects.filter(id = self.id).update(name = val)

   @classmethod
   def get_image_by_id(cls,image_id):
       """
       This is the method to get a specific image
       """
       return cls.objects.get(id = image_id)
    
   @classmethod
   def copy_image(image_url):
        find_image = Image.get_image_by_id(image_id)
        return pyperclip.copy(find_image.image_url)

   @classmethod
   def show_image(cls,category):
        images = cls.objects.filter(category__name=category)
        return images

        
   @classmethod
   def get_photos(cls):
       return cls.objects.all()


   @classmethod
   def search_by_category(cls,category):
        photo = Category.objects.filter(name__icontains = category)[0]
        return  cls.objects.filter(category_id = photo.id)


   def __str__(self):
       return self.name


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','post_date','likes','profile_pic']
        