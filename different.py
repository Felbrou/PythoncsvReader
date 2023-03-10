import csv

with open('different_delim.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'COLUMN NAMES ARE {" ,".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} lives at {row["address"]} and joined on {row["date joined"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')