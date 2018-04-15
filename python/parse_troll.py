import csv
with open('../Data/troll_chat/dota2_chat_messages.csv', 'r', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
