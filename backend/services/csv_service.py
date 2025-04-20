import csv

def generate_csv(data, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

# Example usage:
# data = [{'date': '2023-04-01', 'amount': '150.00', 'description': 'Hotel stay'}, ...]
# generate_csv(data, 'path/to/output.csv')