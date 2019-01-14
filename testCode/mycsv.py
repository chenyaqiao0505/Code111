import xlrd
import csv

def checkformat():
    with open('sale.orderok.csv','r') as f:
        reader = csv.DictReader(f)
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row)

if __name__ == '__main__':
    checkformat()