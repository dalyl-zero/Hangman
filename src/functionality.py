# -*-coding:utf-8 -*

from data import *
from random import randrange
import pickle

def found(player_name):
    """
    Return a boolean to verify whether the key player_name exists in the dictionary scores or not
    """

    if scores.__contains__(player_name):
        return True
    return False

def shuffle():
    """
    Return a string random_word chosen randomly from a file
    """

    with open(filepath["dictionary"], "r") as dictionary:
        words = dictionary.read().split("\n")
        max = len(words) - 1

        # Any word chosen randomly should not be more than 8 characters long
        while True:
            random_index = randrange(max)

            if len(words[random_index]) <= 8:
                break

        random_word = words[random_index]

        return random_word

def hide(random_word):
    """
    Return a string filled with * for the length of the input, random_word
    """

    global hidden_word

    i = 0
    while i < len(random_word):
        # The space added each iteration would be useful to split the string later
        hidden_word += "* "
        i += 1

    return hidden_word

def refresh(player_attempt, hidden_word, random_word):
    """
    Return a string hidden_word with appropriate characters player_attempt
    where found in the string random_word
    """

    hidden_word = hidden_word.split(" ")

    for i, char in enumerate(random_word):
        if char == player_attempt:
            hidden_word[i] = char

    hidden_word = " ".join(hidden_word)

    return hidden_word

def save_score(player_score, player_name):
    """
    Save the score of the current player
    """
    
    scores[player_name] = player_score

    with open(filepath["scores"], "wb") as save_score:
        data_buffer = pickle.Pickler(save_score)
        data_buffer.dump(scores)

def load_score():
    """
    Load and return the scores
    """

    global scores

    with open(filepath["scores"], "rb") as load_score:
        data_buffer = pickle.Unpickler(load_score)
        scores = data_buffer.load()

    return scores

def reset_game():
    """
    Reset game data to default for new game
    """

    global player_name, player_attempt, player_score, random_word, hidden_word,\
    words, scores, filepath, score_counter

    # Player data
    player_name = ""
    player_attempt = ""
    player_score = 0

    # Word data
    random_word = ""
    hidden_word = ""
    words = []

    # File data
    scores = {}
    filepath = {
        "dictionary": "dictionary.txt",
        "scores": "scores",
    }