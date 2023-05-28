import random
import telebot

TOKEN=input("Insert bot token: ")
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def guessinggame(start):
    number=random.randint(1,100)
    tries=0
    bot.send_message(start.chat.id, "Guess my number ranging from 1 to 100!")
    def game():
        @bot.message_handler(content_types=['text'])
        def checkmessage(message):
            nonlocal number
            nonlocal tries
            try:
                int(message.text)
                guess=int(message.text)
            except:
                bot.send_message(message.chat.id, "Enter a number!")
                game()
                return 0
            if guess>100 or guess<1:
                bot.send_message(message.chat.id, "My number is ranged between 1 and 100! \nPlease enter a number in that range.")
                game()
                return 0
            if guess>number:
                bot.send_message(message.chat.id, "Lower!")
                tries+=1
                game()
                return 0
            if guess<number:
                bot.send_message(message.chat.id, "Higher!")
                tries+=1
                game()
                return 0
            if guess==number:
                bot.send_message(message.chat.id, "You won!")
                tries+=1
                bot.send_message(message.chat.id, f"It took you {tries} tries!")
                tries=0
                number=random.randint(1,100)
    game()

bot.polling()