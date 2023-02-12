from django.db import models

# Create your models here.
class Websiteindex(models.Model):
    title_welcome = models.CharField(max_length=150, null=True)
    description_welcome = models.CharField(max_length=600, null=True)
    pic_welcom =models.ImageField( upload_to="WelcomeIndex/%y")
    pic_team =models.ImageField( upload_to="TeamIndex/%y")
    title_team = models.CharField(max_length=150, null=True)
    description_team = models.CharField(max_length=600, null=True)
    team_first_title = models.CharField(max_length=150, null=True)
    team_first_description = models.CharField(max_length=600, null=True)
    team_seconed_title = models.CharField(max_length=150, null=True)
    team_seconed_description = models.CharField(max_length=600, null=True)
    company_title = models.CharField(max_length=160, null=True)
    company_description = models.CharField(max_length=600, null=True)
    pic_company_1 =models.ImageField( upload_to="CompanyIndex/%y")
    pic_company_2 =models.ImageField( upload_to="CompanyIndex/%y")
    pic_company_3 =models.ImageField( upload_to="CompanyIndex/%y")
    customer_title = models.CharField(max_length=160, null=True)
    customer_description = models.CharField(max_length=600, null=True)
    pic_customer_1 =models.ImageField( upload_to="CustomerIndex/%y")
    company_words_title = models.CharField(max_length=160, null=True)
    company_words_description = models.CharField(max_length=600, null=True)
    pic_saying_1 =models.ImageField( upload_to="ImagIndex/%y")
    pic_saying_1_title = models.CharField(max_length=160, null=True)
    pic_saying_2 =models.ImageField( upload_to="ImagIndex/%y")
    pic_saying_2_title = models.CharField(max_length=160, null=True)
    pic_saying_3 =models.ImageField( upload_to="ImagIndex/")
    pic_saying_3_title = models.CharField(max_length=160, null=True)
    manager_title = models.CharField(max_length=300, null=True)
    manager_description = models.CharField(max_length=600, null=True)

    def __str__(self):
        return self.title_welcome
class Montagat(models.Model):
    name = models.CharField(max_length=126)
    price = models.FloatField(max_length=126)
    description = models.CharField(max_length=126)
    location = models.CharField(max_length=126)
    qesm = models.CharField(max_length=126)
    def __str__(self):
        return self.name