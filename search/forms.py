from django.forms import *

class SearchForm(Form):

    keywords = CharField(
        max_length = 20,
    
        min_length = 1,

        required = True
    )