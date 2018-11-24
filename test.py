import csv

filename = "bearsbikes1.csv"

with open(filename) as f: # Open the file and store it in "f"
    reader = csv.reader(f) # Make a reader object associated with the file
    header_row = next(reader) # Returns the NEXT line of the header
    print(header_row) # Prints the output

    # Here, we want the index number and column header
    # "Enumerate" gets the index number and value of each item in the list
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # To read specefic parts of the data, one can parse the data by row
    # Then, the value associated with the specefic column one is looking at
    # Can be printed

    for index, line in enumerate(reader):
        print(index, line)

    
    for line in reader:
        print(next(reader))
        


    status = []

    phone_numbers = []

    """
    try:
        for row in reader:
            item = row[1]
            status.append(item)
            print(item)
    except UnicodeDecodeError:
        print("Sorry, there was an error.")
    

    for row in reader:
        phone_numbers.append(row[9])

    for item in phone_numbers:
        print(item)
    """           

    


"""
for index in status:
    if "In Store" in index:
        print("not finished")
"""




