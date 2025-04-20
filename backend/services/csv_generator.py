import csv

def read_hotel_receipt_data(input_file):
    data = []
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data