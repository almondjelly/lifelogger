from random import choice

quotes_file = open("quotes.txt")
quotes_dict = {}

counter = 0

for line in quotes_file:
    line = line.rstrip()
    if line:
        quotes_dict[counter] = "{}".format(line)
        counter += 1


def choose_quote():
    return choice(quotes_dict)
    

def display_quotes():
    quote_list = []

    for value in quotes_dict.values():
        quote_list.append(value)

    return quote_list