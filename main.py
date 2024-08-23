### Morse Code Interpreter
import pandas as pd

# get the word to interpret
user_word = input("Please, write down the word to encode: ")
user_word_list = list(user_word.upper())

# set up the dict with the code from csv using pandas
data = pd.read_csv("morsecode.csv")
data_dict = {row.letter: row.morsecode for (index, row) in data.iterrows()}

# encode the word using list comprehension
encoded_message = [data_dict[letter] for letter in user_word_list]
print("Here is your encryption: ")
print(*encoded_message)



