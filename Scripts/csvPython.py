import csv
with open('cars.csv', 'r') as csv_car:
    csv_reader = csv.reader(csv_car, delimiter=';')
    for row in csv_reader:
        print(row)
