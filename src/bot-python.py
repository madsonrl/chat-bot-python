# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot

bot = ChatBot('Teste')

conv = ['Oi', 'Olá', 'Olá, Bom Dia', 'Bom dia, Como Vai?', 'Estou Bem']

conv2 = ['Qual seu filme preferido?', 'Eu gosto de Deadpool', 'Como se chama?', 'Meu nome é Robin']

# Coordenação em geral#
conv3 = ['Qual é o diretor', 'O Diretor do ICET é o Prof. Dr. Jorge Yoshio Kanda']
conv4 = ['Qual o Coordenador Acadêmico', 'O Coordenador Acadêmicodo ICET é o Prof. Dr. Geone Maia Correa']
conv5 = ['Qual é a Coordenadora Administrativa','A Coordenadora Administrativa é a Técnica em Contabilidade, Bel. e Lic. Kátia Rejane da Silva Rufino']

# CURSO DE AGRONOMIA#
conv6 = ['quem é o coordenador de Agronomia?','É o Gerlândio Suassuna Gonçalves']
conv7 = ['quem é o Vice-coordenador de Agronomia?','É o Arthur Antunes de Souza Cardoso']
conv8 = ['Qual a duração de agronomia?','No mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# ENGENHARIA DE SOFTWARE
conv9 = ['Qual o coordenador de Engenharia de Software?','É o Carlos Alberto da Costa Barata']
conv10 = ['Qual o Vice-coordenador de Engenharia de Software?','É a Daniella de Oliveira Costa']
conv11 = ['Qual a duração de Engenharia de Software?','O curso de Engenharia de Software dura no mínimo 5 anos (10 semestres) e no maxímo 7,5 anos (15 semestres)']

# Engenharia de Produção#
conv12 = ['como se chama o coordenador de Engenharia de Produção?','É a Rute Holanda Lopes']
conv13 = ['como se chama o Vice-coordenador de Engenharia de Produção?','Desculpe mas eu não sei quem é o Vice-coordenador de Engenharia de Produção']
conv14 = ['qual o tempo de duração de Engenharia de Produção?','O curso de Engenharia de Produção dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# Engenharia Sanitária#
conv15 = ['quem é o coordenador de Engenharia Sanitária?','É a Suéllenn dos Santos Hinnah']
conv16 = ['quem é o Vice-coordenador de Engenharia Sanitária?','É o Ricardo Takashi Kuwano']
conv17 = ['Quanto tempo dura o curso Engenharia Sanitária?','O curso de Engenharia Sanitária dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# Farmácia#
conv18 = ['Qual o coordenador de Farmácia?', 'É o Aluízio Gonçalves Brasil Jr.']
conv19 = ['Qual o Vice-coordenador de Farmácia?','É o Paulo Maximiliano Corrêa']
conv20 = ['Qual a duração de Farmácia?','O curso de Farmácia dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# Química Industrial#
conv21 = ['Quem é o coordenador de Química Industrial?','É a Margarida Carmo de Souza']
conv22 = ['Quem é o Vice-coordenador de Química Industrial?','É o Hidelbrando Ferreira Rodrigues']
conv23 = ['Qual a duração de Química Industrial?','O curso de Química Industrial dura no mínimo 4 anos (8 semestres) e no maxímo 8 anos (16 semestres)']

# Sistemas de Informação#
conv24 = ['Qual o coordenador de Sistemas de Informação?','É a Odette Mestrinho Passos']
conv25 = ['Qual o Vice-coordenador de Sistemas de Informação?','É a Anacília Maria Cavalcante de Almeida Palmeira Vieira']
conv26 = ['Qual a duração de Sistemas de Informação?','O curso de Sistemas de Informação dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# Química e Biologia#

conv27 = ['Qual o coordenador de Química e Biologia?','É o Dominique Fernandes de Moura do Carmo']
conv28 = ['Qual o Vice-coordenador de Química e Biologia?','É o Paulo José de Sousa Maia']
conv29 = ['Qual a duração de Química e Biologia?','O curso de Química e Biologia dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']

# Matemática e Física
conv30 = ['Qual o coordenador de Matemática e Física?','É o Marco Aurélio dos Santos Cruz']
conv31 = ['Qual o Vice-coordenador de Matemática e Física?','É o Sandro Simas de Jesus']
conv32 = ['Qual a duração de Matemática e Física?','O curso de Matemática e Física dura no mínimo 5 anos (10 semestres) e no maxímo 10 anos (20 semestres)']


conv33 = ['Quais os Cursos que o icet oferece?' , 'Os cursos ofertados pelo icet são: Agronomia, Engenharia de Software, Engenharia de Produção, Engenharia Sanitária, Farmácia, Química Industrial, Sistemas de Informação, Licenciatura em Ciências: Química e Biologia e Licenciatura em Ciências: Matemática e Física']

conv34 = ['onde fica a biblioteca?','Fica no bloco F']
conv35 = ['Onde fica as salas dos professores?','Fica no bloco F']
conv36 = ['Que horas começam as refeições?','O café é das 7-9h, o almoço é das 11-13h30 e o jantar das 17-19h']
conv37 = ['como faço para ver minhas notas?','As notas assim como as faltas podem ser visualizadas no site ecampus.ufam.edu.br']
conv38 = ['Em qual bloco fica o auditorio?','O auditorio fica no bloca A']

bot.set_trainer(ListTrainer)

bot.train(conv)
bot.train(conv2)
bot.train(conv3)
bot.train(conv4)
bot.train(conv5)
bot.train(conv6)
bot.train(conv7)
bot.train(conv8)
bot.train(conv9)
bot.train(conv10)
bot.train(conv11)
bot.train(conv12)
bot.train(conv13)
bot.train(conv14)
bot.train(conv15)
bot.train(conv16)
bot.train(conv17)
bot.train(conv18)
bot.train(conv19)
bot.train(conv20)
bot.train(conv21)
bot.train(conv22)
bot.train(conv23)
bot.train(conv24)
bot.train(conv25)
bot.train(conv26)
bot.train(conv27)
bot.train(conv28)
bot.train(conv29)
bot.train(conv30)
bot.train(conv31)
bot.train(conv32)
bot.train(conv33)
bot.train(conv34)
bot.train(conv35)
bot.train(conv36)
bot.train(conv37)
bot.train(conv38)
while True:
    quest = input('Você: ')

    response = bot.get_response(quest)

    if float(response.confidence > 0.5):
        print('Bot:', response)
    else:
        print('Bot: Não endendi')
