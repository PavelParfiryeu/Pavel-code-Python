allword = ["междометье", "наречие", "дополнение"]
import random
comp_word = random.choice(allword)
word_new = []
live = 14
print(f"Отгадайте часть речи. У вас {live} попыток")
for letter in comp_word:
    word_new.append(letter)
my_word = []
for letter in word_new:
    my_word.append("*")
while live > 0:
    print(f"Загаданное слово: ")
    print(my_word)
    a = input("Введите букву: ")
    if a =="exit":
        break
    if a not in word_new:
        live = live - 1
    for letter in word_new:
        if letter ==a:
            print("Такая буква есть!")
            my_word[word_new.index(letter)] = letter
            live = live - 1
    print(f"Осталось попыток {live}!")
    if my_word == word_new:
        print("Вы угадали! Игра окончена!")
        break
else:
    print(f"Вы проиграли. Это было слово {comp_word}")