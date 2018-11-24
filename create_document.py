import csv

filename = "bb2.csv"

with open(filename) as f: # Open the file and store it in "f"
    reader = csv.reader(f) # Make a reader object associated with the file
    header_row = next(reader) # Returns the NEXT line of the header
    print(header_row) # Prints the output

    for index, line in enumerate(reader):
        print(index)
        for item in line:
            print(item)

    
