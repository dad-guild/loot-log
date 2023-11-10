#!/usr/bin/env python3
import csv, re, sys

# Parse a line into its parts for CSV export
def parse_line(line):
    match = re.match(r'^(\S+) - (.*) \(([0-9]+)\) ((?:MS)|(?:OS)|-) ([0-9]{4}-[0-9]{2}-[0-9]{2}).*$', line)
    fields = list(match.group(1, 2, 3, 4, 5))
    fields[3] = 1 if fields[3] == 'OS' else 0
    return fields

def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <file>')
        exit(1)

    in_filename = sys.argv[1]
    out_filename = re.sub(r'(\.[a-z]+)?$', '.csv', in_filename, count=1)

    # Parse each line from the input
    with open(in_filename) as f:
        items = [parse_line(line) for line in f]

    # Write the output csv
    with open(out_filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        [writer.writerow(item) for item in items if item[0] != '_disenchanted']

if __name__ == "__main__":
    main()
