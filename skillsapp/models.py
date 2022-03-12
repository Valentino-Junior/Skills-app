
from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt


class Skills(models.Model):
    
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    def save_skill(self):
        self.save()
        
    def delete_skill(self):
        self.delete()
    
    @classmethod
    def update_skill(cls, cat_id, value):
        cls.objects.filter(id=cat_id).update(name=value)


        
class Profile(models.Model):
    potrait = CloudinaryField('potrait')
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    skill = models.ManyToManyField(Skills, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def update_profile_name(cls,id,name):
        update =cls.objects.filter(id=id).update(name=name)
        return update

    @classmethod
    def update_profile(cls, id, potrait):
        update = cls.objects.filter(id=id).update(potrait=potrait)
        return update


       
    @classmethod
    def get_profile_by_id(cls, id):
        potrait = cls.objects.filter(id=id).all()
        return potrait

    
    @classmethod
    def search_by_skill(cls, search_term):
        potraits = cls.objects.filter(skill__name__icontains=search_term)
        return potraits
    
    
    class Meta:
        ordering = ['-upload_date']
  

