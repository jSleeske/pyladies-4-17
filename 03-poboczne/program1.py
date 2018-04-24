
def my_awesome_function(sender):
    template = 'Called from {sender}, current __name__ value is: {value}'
    print(template.format(sender=sender, value=__name__))


print('Welcome to my amazing program!')
print('Running my awesome function...')
my_awesome_function('top of program1')
