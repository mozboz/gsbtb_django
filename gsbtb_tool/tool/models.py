from django.db import models

class Person(models.Model):

    GERMAN_NO = 'NO'
    GERMAN_SOME = 'SOME'
    GERMAN_YES = 'YES'

    GERMAN_CHOICES = (
        (GERMAN_NO, 'None'),
        (GERMAN_SOME,  'Some'),
        (GERMAN_YES, 'Yes')
    )

    # tidy these up, use better types, etc.
    given_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    email = models.EmailField()
    personal_website = models.URLField()
    image = models.ImageField()
    german_skills = models.CharField(max_length=4, choices=GERMAN_CHOICES, default=GERMAN_NO)
    gender = models.CharField(max_length=2)
    about_me = models.TextField(max_length=1024, default="")
    my_idea = models.TextField(max_length=1024, default="")

    def __unicode__(self):
        return u'%s %s' % (self.given_name, self.family_name)


class Project(models.Model):
    project_name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % (self.project_name)



class Skill(models.Model):
    name = models.CharField(max_length=256)


class Opportunity(models.Model):
    # @todo set some status options
    status = models.IntegerField()
    person = models.ForeignKey(Person)
    project = models.ForeignKey(Project)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)