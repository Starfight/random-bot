#!/usr/bin/env python
# coding: utf8
# Random bot for a unknown site
# @author: Nicolas Drufin <nicolas.drufin@ensc.fr>

import os
import sys
from optparse import OptionParser
from randbotlib.bot import Bot


def main(args):
    # parse arguments options
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", dest="nb", default=1, help="Number of redirection")
    parser.add_option("-w", "--word", type="string", dest="word", help="A word or url to start")
    (options, _) = parser.parse_args()

    # verify option
    if options.nb <= 0:
        print "Option --number need to be positive"
        return 1

    while not options.word:
        options.word = raw_input("Enter something: ")

    bot = Bot()
    word = options.word
    for i in range(0, options.nb):
        word = bot.pick_link_from(word, bot.is_url(options.word))
        if not word:
            break

    if word:
        print "Here we are: %s" % bot.last_url

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
