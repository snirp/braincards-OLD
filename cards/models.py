from django.db import models
from braincards.settings import AUTH_USER_MODEL
from ordered_model.models import OrderedModel


class Owner(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    notify_proposed_question = models.BooleanField(default=True)


class Website(models.Model):
    name = models.CharField(max_length=254)
    shortname = models.SlugField(max_length=50)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Domain(models.Model):
    """ Approved domains for loading a publication """
    domain = models.URLField()
    website = models.ForeignKey(Website, on_delete=models.CASCADE)


class Page(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=254)
    identifier = models.CharField(max_length=50)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Question(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    question = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True,  on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    order_with_respect_to = 'page'


class Choice(OrderedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()
    correct = models.BooleanField(default=False)
    order_with_respect_to = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    correct = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
