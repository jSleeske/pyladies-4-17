
def my_awesome_function(sender):
    template = 'Called from {sender}, current __name__ value is: {value}'
    print(template.format(sender=sender, value=__name__))


if __name__ == '__main__':
    print('Welcome to my amazing program!')
    print('Running my awesome function...')
    my_awesome_function('__name__ == __main__ of program2')
