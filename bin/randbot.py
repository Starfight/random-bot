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

    bot = Bot()
    word = options.word
    for i in range(0, options.nb):
        word = bot.pick_link_from(word)

    print "Here we are: %s" % word

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
