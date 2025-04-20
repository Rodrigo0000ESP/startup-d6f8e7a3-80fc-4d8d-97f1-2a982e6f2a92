def generate_csv(data_list):
    import csv
    from io import StringIO

    # Define the CSV schema columns
    fieldnames = ['Date', 'Item', 'Category', 'Amount']

    # Create a StringIO buffer to write the CSV data
    csv_buffer = StringIO()
    csv_writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the data rows
    for data in data_list:
        csv_writer.writerow(data)

    # Get the CSV string from the buffer
    csv_string = csv_buffer.getvalue()
    csv_buffer.close()

    # Optionally save the CSV string to a file or return it
    # For saving to file, additional code would be needed

    return csv_string