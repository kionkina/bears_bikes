import csv

filename = "bearsbikes1.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)



    for index, column_header in enumerate(header_row):
        print(index, column_header)

    try:
        status = []
        for row in reader:
            status.append(row[1])
            # print(status)
    except UnicodeDecodeError:
        pass


for index in status:
    if "In Store" in index:
        print("not finished")
        

