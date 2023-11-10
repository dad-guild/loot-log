#!/usr/bin/env python3
import csv, re, sys, datetime

# player,date,time,id,item,itemID,itemString,response,votes,class,instance,boss,difficultyID,mapID,groupSize,gear1,gear2,responseID,isAwardReason,subType,equipLoc,note,owner

def parse_record(record):
    return [
        record[0].split('-')[0],
        record[4].strip('[]'),
        int(record[5]),
        1 if record[7] == 'Offspec/Greed' else 0,
        datetime.datetime.strptime(f'{record[1]} {record[2]}', '%m/%d/%y %H:%M:%S'),
    ]

def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <file>')
        exit(1)

    in_filename = sys.argv[1]
    out_filename = re.sub(r'(\.[a-z]+)?$', '.csv', in_filename, count=1)

    # Parse each line from the input
    with open(in_filename) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        items = [parse_record(record) for record in reader]

    # Write the output csv
    with open(out_filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        [writer.writerow(item) for item in items if item[0] != '_disenchanted']

if __name__ == "__main__":
    main()
