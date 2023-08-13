

from django.db import models

# Create your models here.



QUESTION
id
order(sequence maintain)
text                                        Favourite subject ??
type(checkbox, radio, text)                 

OPTION
id
question_id - Foreign to Questions
text                                        English YGeographical Yscience

ANSWER
id
q_id                                        1_id = 1
option_id                                   1 - YGeographical   2 - Science
text                                        
user_id                                     requested User

question has many options

answer belongs to question
answer belongs to option





