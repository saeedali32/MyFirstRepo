import csv

class Order:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink

round = [Order("John", "Coffee"), Order("Sally", "Tea"), Order("Mark", "Coke"), Order("Lisa", "Beer")]

try:
    with open('round.csv', 'w') as csvfile:
        round_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for order in round:
            round_writer.writerow([order.name, order.drink])
except:
    print("Unable to write round")

orders = []

try:
    with open('round.csv', 'r') as csvfile:
        round_reader = csv.reader(csvfile)
        for row in round_reader:
            orders.append(Order(row[0], row[1]))
except:
    print("Unable to read round")
for order in orders:
    print(order.name + " : " + order.drink)