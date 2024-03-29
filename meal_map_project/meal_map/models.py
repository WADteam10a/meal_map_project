from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[0-9]+$', 'Only numeric characters are allowed.')

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reviewer")
    profile_picture = models.ImageField(upload_to="reviewer_pics", blank=True)

    class Meta:
        verbose_name_plural = "Reviewers"

    def __str__(self):
        return self.user.username

class RestaurantOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="restaurant_owner")
    restaurant_name = models.CharField(max_length=128, default="Your Restaurant")
    profile_picture = models.ImageField(upload_to="owner_pics", blank=True)

    class Meta:
        verbose_name_plural = "Restaurant Owners"

    def __str__(self):
        return self.restaurant_name

class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    phone_number = models.CharField(validators =[numeric], max_length=32)
    opening_hours = models.CharField(max_length=128)
    website = models.URLField(max_length=128)
    rating = models.SmallIntegerField(default = 0)
    food_type = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="restaurant_photos/")
    owner = models.OneToOneField(RestaurantOwner, on_delete=models.CASCADE, related_name='restaurant')
    slug = models.SlugField(unique=True, default='default-slug')
 
    def calculate_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / len(reviews)
            return round(average_rating, 1)
        return 0.0
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_text = models.TextField()
    rating = models.SmallIntegerField(validators =[MaxValueValidator(5), MinValueValidator(1)])
    date = models.DateTimeField()
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviews')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return _("Review by {} on {}").format(self.reviewer, self.date)
