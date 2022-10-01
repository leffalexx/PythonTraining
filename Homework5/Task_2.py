# Создайте программу для игры с конфетами человек против человека.

from random import randint

def game(total):
    while True:
        answer = int(input('Сколько конфет вы хотите взять? '))
        if not answer in range(1, 29):
            print('Вы можете взять от 1 до 28 конфет за ход. Попробуйте еще раз!')
            continue
        if answer > total:
            print(f'На столе осталось {total} конфет! Забирайте их и празднуйте победу!')
            continue
        total -= answer
        print(f'Осталось {total} конфет')
        return total
        break

def game_engine(candies, player1, player2):
  turn = 0
  while candies !=0:
      candies = game(candies)
      turn += 1
  if turn % 2 == 0:
    print(f'{player2} победил и забирает все конфеты!')
  else:
    print(f'{player1} победил и забирает все конфеты!')

print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
\nВсе конфеты оппонента достаются сделавшему последний ход. Начинаем игру!\
\nПервым ходит Игрок 1')
candies = 2021
player1 = 'Игрок 1'
player2 = 'Игрок 2'
game_engine(candies, player1, player2)