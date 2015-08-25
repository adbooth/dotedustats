from sys import argv
from HTMLParser import HTMLParser


class TagCounter(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        # Basic tag counting fields
        self.tagcount = 0
        self.nonvoid_tagcount = 0
        # Nest counting fields
        self.tagdepths = [0]
        self.tagstack = []

    # Called on opening tags
    def handle_starttag(self, tag, attrs):
        self.tagstack.append(tag)
        self.tagcount += 1
        if len(self.tagstack) > self.tagdepths[-1]:
            self.tagdepths.append(len(self.tagstack))

    # Called on closing tags
    def handle_endtag(self, tag):
        self.tagcount += 1
        self.nonvoid_tagcount += 1

        # Get top tag and compare to current tag
        # Go back down the line if a mistake was made
        top = self.tagstack.pop()
        while tag != top:
            self.tagdepths.pop()
            top = self.tagstack.pop()


    # Called on singlton tags
    def handle_startendtag(self, tag, attrs):
        self.tagcount += 1
        if len(self.tagstack)+1 > self.tagdepths[-1]:
            self.tagdepths.append(len(self.tagstack)+1)

    def feed(self, data):
        HTMLParser.feed(self, data)
        self.topnest = self.tagdepths[-1]
