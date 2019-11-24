"""
__author__ = Paul Basso

"""


def randomsites():
    """
Opens a random website from a created list already in the code.

    """

    import webbrowser
    import random

    websites = ['http://google.com/', 'http://youtube.com/',
                'http://reddit.com/', 'http://www.sporcle.com/',
                'http://www.15facts.com/',
                'http://www.findtheinvisiblecow.com/',
                'http://www.instructables.com/',
                'http://www.howstuffworks.com/', 'https://theuselessweb.com/']

    webbrowser.open(random.choice(websites))
