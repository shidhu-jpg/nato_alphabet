import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data.to_dict(data)
dict12 = { row.letter:row.code for (index,row) in data.iterrows()}


# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# . Create a list of the phonetic code words from a word that the user inputs.
user = input("type here").upper()
namee_code = [dict12[letter] for  letter in user if letter in dict12]
print(namee_code)