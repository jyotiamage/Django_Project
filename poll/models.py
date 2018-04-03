from django.db import models

import datetime
from django.utils import timezone

relation_ship=(
	("father", "Father"),
	("mother", "Mother"),
	("care_taker","Care Taker"),
	("guardian","Guardina"),	)
)

gender=(
	("M","Male")
	("F","Female")
)

class Parent(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	relation = models.CharField(max_length=20, choices=relation_ship)
	gender = models.CharField(max_length=20, choices=gender)

class Child(models.Model):
	parent = models.ForeignKey(Parent, related_name='children')
	child_name = models.CharField(max_length=200)
	gender = models.CharField(max_length=20, choices=gender)


class Question(models.Model):
	question_text= models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text



class Choice(models.Model)	:
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

