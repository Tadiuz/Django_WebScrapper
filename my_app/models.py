from django.db import models

# Create your models here.

#First model called search, it takes an input
#This class here is like the first column of our database,a nd it will store all the information
class Search(models.Model):

    search = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now=True)

    #This part is to show the name of what we are searching instead of the id like iwthout it it will be _01923021 but wiht it it will be the owrd we searched like "blah blah"
    def __str__(self):
        return '{}'.format(self.search)

    #This part is for the format of the word searches, how it will lock in the interface
    class Meta:

        verbose_name_plural = 'Searches'
