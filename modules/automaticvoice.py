from sopel.module import rule, event

@event('JOIN')
@rule(r'.*')
def autovoice(bot, trigger):
    """Gives voice to any user that connects to the channel and gives them the welcome message."""
    if trigger.is_privmsg:
        return 0
    channel = trigger.sender
    nick = trigger.nick
    bot.write(['MODE', channel, "+v", nick])
    bot.notice("""Hey, I'm a bot. Use ".help" to get a list of commands to use on me.""", nick)
    return 0
