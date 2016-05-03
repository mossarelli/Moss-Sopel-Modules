# coding=utf-8
"""
help.py - Sopel Help Module
Copyright 2008, Sean B. Palmer, inamidst.com
Copyright © 2013, Elad Alfassa, <elad@fedoraproject.org>
Licensed under the Eiffel Forum License 2.

http://sopel.chat
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import textwrap
import collections

#from sopel.formatting import bold
from sopel.module import commands, rule, example, priority

@rule('$nick' '(?i)(test|test) +([A-Za-z]+)(?:\?+)?$')
@example('.test tell')
@commands('test')
@priority('low')
def testtest(bot, trigger):
    """Shows a command's documentation, and possibly an example."""
    #bot.say(trigger.sender())
    print("Test")
    return "string"
