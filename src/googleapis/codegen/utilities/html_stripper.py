#!/usr/bin/python3
import html.parser as HTMLParser

# Copyright 2011 Google Inc. All Rights Reserved.

"""HTMLStripper based on HTMLParser."""


__author__ = 'wclarkso@google.com (Will Clarkson)'


class HTMLStripper(HTMLParser.HTMLParser):
    """Simple class to strip tags from HTML."""

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def GetFedData(self):
        return ''.join(self.fed)

    def ClearFedData(self):
        self.fed = []

    def feed(self, data):
        super(HTMLStripper, self).feed(data)
