import telepot as tele #Importando a bibliotec telepot
from chatterbot import ChatBot #Importando o modulo ChatBot da biblioteca Chatterbot
from chatterbot.trainers import ListTrainer #impoando o modulo ListTrainer da biblioteca chatterbot

f = open('conversa.txt','r')#abrindo o txt com o dicionario para o bot fazer as interações
arq = f.readlines() #Retornando cada linha do txt como elemento de uma lista
bot = ChatBot("Meubot") #Criando o bot
trainer = ListTrainer(bot)#Treinando o bot
trainer.train(arq)#Treinando o bot com o dicionario contido na variavel f
api = '721682439:AAGZhipkNu3CLm6PJ4OLO4mYPdg1blxstV0'#chamando o bot do telegram
def receber(msn):#criando uma função para receber mensagens do telegram
    text = msn['text']#procurando linha json que contem o texto enviado pelo bot
    _id = msn['from']['id']#procurando linha json que contem quem enviou a mensagem e qual o id da mesma.
    nome = msn['from']['first_name']#procurando linha json que contem quem enviou a mensagem e o primeiro nome do mesmo.
    if "ola" in text:#Caso na variavel text exista um ola, o bot respondera ola + o nome do usuário
        telegram.sendMessage(_id ,"Ola,"+str(nome))
    else:
        telegram.sendMessage(_id,str(bot.get_response(text)))#senão, ele utilizará o dicionario da variavel arq


telegram = tele.Bot(api)#Fazendo integração com o Telegram
telegram.message_loop(receber)#criando um loop com a função receber
while True:#Cria um while para deixar os comandos rodando.
    pass


