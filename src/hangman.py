# -*-coding:utf-8 -*

import os
from data import *
from functionality import *

global score_counter

while True:
    # Make sure the scores file exists
    try:
        open(filepath["scores"], "rb")
        scores = load_score()

    except FileNotFoundError:
        open(filepath["scores"], "xb")

    print("HANGMAN")
    print("_______\n")

    player_name = input("What is your name ? ")

    if player_name.isspace() or player_name == "":
        print("\nYou must enter a name\n")
        continue

    if not found(player_name):
        scores[player_name] = 0
        save_score(player_score, player_name)

    random_word = shuffle()
    hidden_word = hide(random_word)

    while score_counter > 0:
        print("\n")

        print(hidden_word)
        # Debug
        print(random_word)

        print("You have {}".format(score_counter) + " chance(s) left")
        player_attempt = input("Guess a letter: ")
        player_attempt = player_attempt.upper()

        hidden_word = refresh(player_attempt, hidden_word, random_word)

        if hidden_word.replace(" ", "") == random_word:
            print("\nCongratulations, You Won !\n")
            break

        score_counter -= 1

        if score_counter == 0:
            print("\nGame Over\n")

    player_score = scores[player_name]   
    print("Your previous score was: {}".format(player_score))

    player_score = 8 - score_counter
    save_score(player_score, player_name)

    player_attempt = input("\nDo you want to replay ? (Y/N) ")

    print("\n")

    if player_attempt.upper() == "Y":
        reset_game()
        score_counter = 8
        continue
    else:
        print("Goodbye !")
        break

os.system("pause")