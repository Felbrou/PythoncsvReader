import csv

with open('lista_livros.csv') as csv_file:
    csr_reader = csv.DictReader(csv_file, delimiter=',')
    line_counter = 0
    for row in csr_reader:
        if line_counter == 0:
            print(f'column names are {", ".join(row)}"')
            line_counter += 1
        print(f'\tBook:{row["title"]} Rating: {row["rating"]} Author:{row["name"]}')
        line_counter += 1
    print(f'Processed {line_counter} lines')