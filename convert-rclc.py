#!/usr/bin/env python3
import csv, re, sys, datetime

def convert_row(row):
    return [
        row['player'].split('-')[0],
        row['item'].strip('[]'),
        int(row['itemID']),
        1 if row['response'] == 'Offspec/Greed' else 0,
        datetime.datetime.strptime(f'{row["date"]} {row["time"]}', '%m/%d/%y %H:%M:%S'),
    ]

def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <file>')
        exit(1)

    in_filename = sys.argv[1]
    out_filename = re.sub(r'(\.[a-z]+)?$', '.csv', in_filename, count=1)

    # Parse each line from the input
    with open(in_filename) as f:
        reader = csv.DictReader(f)
        items = [convert_row(x) for x in reader]

    print(items)

    # Write the output csv
    with open(out_filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(('character', 'itemName', 'itemID', 'offspec', 'date'))
        [writer.writerow(item) for item in items if item[0] != '_disenchanted']

if __name__ == "__main__":
    main()
