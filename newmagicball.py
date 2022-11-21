import random
messages = ['It is certain',
 'It is decidedly so',
 'Yes definitely',
 'Reply hazy try again',
 'Ask again later',
 'Concentrate and ask again',
 'My reply is no',
 'Outlook not so good',
 'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)]) 
# we put the -1 because len messaged will give nine, but index starts from zero
#therefore we subtract the last index (9) which doesnt exist ;)