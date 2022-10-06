# Добавьте игру против бота

from random import randint

def bot(candies_amount, max):
  if candies_amount < max:
    max = candies_amount
  bot_candies = randint(1, max+1)
  print(f'Бот взял {bot_candies} конфет')
  candies_amount -= bot_candies
  print(f'Осталось {candies_amount} конфет')
  return candies_amount
  

def user(candies_amount):
    while True:
        taken_candies = int(input('Возьмите от 1 до 28 конфет '))
        candies_amount -= taken_candies
        print(f'Осталось {candies_amount} конфет')
        return candies_amount
        break

def game(candies):
  turn = 0
  while candies > 0:
    candies = user(candies)
    turn += 1
    candies = bot(candies, 28)
    turn +=1
  if turn % 2 == 0:
    print('Игрок 1 победил и забирает все конфеты!')
  else:
    print('Бот победил и забирает все конфеты!')
  

candies = 2021
print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
\nВсе конфеты оппонента достаются сделавшему последний ход. Начинаем игру!\
\nПервым ходит Игрок 1')

game(candies)