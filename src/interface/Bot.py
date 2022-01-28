# -*- coding: utf-8 -*-

from chatterbot.trainers  import ListTrainer

from chatterbot import ChatBot

bot = ChatBot ('Teste')

conv = ['Oi', 'Olá', 'Olá, Bom Dia', 'Bom dia, Como Vai?', 'Estou Bem'] 

conv2 = ['Qual seu filme preferido?', 'Eu gosto de Dead Pool', 'Como se chama?','Meu nome é Robin']


bot.set_trainer(ListTrainer)

bot.train(conv)
bot.train(conv2)

while True:
	quest = input('Você: ')

	response = bot.get_response(quest)

	if float(response.confidence > 0.5):
		print('Bot:', response)
	else:
		print('Bot: Não endendi')		 
