import telebot
bot=None
def init_bot(token):
    global bot
    bot=telebot.TeleBot('823664291:AAEfuC8rMJ4eRke2vSrdUsHy7h67RkPO3cE')
    telebot.apihelper.proxy={
# 'https': 'http://138.68.166.224:8080'
'https': 'http://54.37.136.149:3128'
}
    import handlers