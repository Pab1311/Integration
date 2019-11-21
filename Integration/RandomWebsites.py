import webbrowser
import random

def randomsites():
    websites = ['http://google.com/', 'http://youtube.com/', 'http://reddit.com/', 'http://www.sporcle.com/'
                , 'http://www.15facts.com/', 'http://www.findtheinvisiblecow.com/', 'http://www.instructables.com/',
                'http://www.howstuffworks.com/', 'https://theuselessweb.com/']

    webbrowser.open(random.choice(websites))
