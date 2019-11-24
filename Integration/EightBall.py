"""
__author__ = Paul Basso

"""


def eightball(name):
    """
Acts as a Magic Eight Ball for the user to ask questions about their future.

    :param name:
    """

    import random
    input("What is your question? ")
    eightstatements = [
        'Ask again later,',
        'Better not tell you now,',
        'Cannot predict now,',
        'Concentrate and ask again,',
        'Don’t count on it,',
        'It is certain,',
        'It is decidedly so,',
        'Most likely,',
        'My reply is no,',
        'My sources say no,',
        'Outlook not so good,',
        'Outlook good,',
        'Signs point to yes,',
        'Very doubtful,',
        'Without a doubt,',
        'Yes,',
        'Yes – definitely,']
    print(random.choice(eightstatements), "%s" % name)
