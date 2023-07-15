from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class UserInfo(TranslatableModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    translations = TranslatedFields(
        title = models.CharField(_('Title'),max_length=255,null=True,blank=True),
        full_name = models.CharField(_('Full name'),max_length=200,null=True,blank=True),
        address = models.CharField(_("Adress"),max_length=200,null=True,blank=True),
        bio = models.TextField(_("Bio"),null=True,blank=True),
        cv = models.FileField(upload_to='CV/',null=True,blank=True),
    )
    experince = models.IntegerField(default=0,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    @property
    def projects(self):
        return self.user.portfolio_set.all().count()

    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("UserInfo")

    # def __str__(self):
    #     return self.title

class Services(TranslatableModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    icon = models.CharField(max_length=200,null=True,blank=True)
    translations = TranslatedFields(
        title = models.CharField(_('Title'),max_length=200,null=True,blank=True),
        desciption = models.TextField(_('Description'),null=True,blank=True)
    )


    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Services")

    def __str__(self):
        return str(self.id)

class Education(TranslatableModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    translations = TranslatedFields(
        degree = models.CharField(_('Degree'),max_length=200,null=True,blank=True),
        education_place = models.TextField(_('Education place'),null=True,blank=True),
        desciption = models.TextField(_('Description'),null=True,blank=True)
    )
    education_years = models.CharField(_("Years"),max_length=20,null=True,blank=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Education")

    def __str__(self):
        return str(self.id)

class Experience(TranslatableModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    translations = TranslatedFields(
        job_title = models.CharField(_('Job title'),max_length=200,null=True,blank=True),
        work_place = models.TextField(_('Work place'),null=True,blank=True),
        desciption = models.TextField(_('Description'),null=True,blank=True)
    )
    work_years = models.CharField(_("Years"),max_length=20,null=True,blank=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Experience")

    def __str__(self):
        return str(self.id)

class Skills(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    skill_name = models.CharField(_("Skill Name"),max_length=150,null=True,blank=True)
    percent = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Skills")

    def __str__(self):
        return str(self.id) 

class Portfolio(TranslatableModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    translations = TranslatedFields(
        title = models.CharField(_('Title'),max_length=200,null=True,blank=True),
        desciption = models.TextField(_('Description'),null=True,blank=True),
    )
    image = models.ImageField(upload_to='Projects/',null=True,blank=True)
    type = models.CharField(max_length=20,null=True,blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Portfolio")

    def __str__(self):
        return str(self.id)

class Cuntuct_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Cuntuct_us")

    def __str__(self):
        return self.name

