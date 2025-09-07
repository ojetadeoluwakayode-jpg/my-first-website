from django.db import models


class Sign_in(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    jambscore = models.IntegerField(null=True)
    email_address = models.EmailField(max_length=50, null=True)
    slug = models. SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
