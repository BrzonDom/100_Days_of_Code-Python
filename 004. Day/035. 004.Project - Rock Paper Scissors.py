"""
  4. Project - Rock Paper Scissors

    You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about
    randomisation and Lists to achieve this.

    Demo:
        https://appbrewery.github.io/python-day4-demo/

"""


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options_word = {0: "Rock",
                1: "Paper",
                2: "Scissors"}

options_print = {0: rock,
                 1: paper,
                 2: scissors}

options_beats = {0: 2,
                 1: 0,
                 2: 1}
