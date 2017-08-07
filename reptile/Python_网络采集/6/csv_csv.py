import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import StringIO

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii','ignore')
csvfile = StringIO(data)

# #打印
# csvReader = csv.reader(csvfile)
# for row in csvReader:
#     print(row)

#保存csv
csv_File = open('../6/csv/csv.csv','wt',newline='',encoding='utf-8')
writer =csv.writer(csv_File)
try:
    for row in csvfile:
        print(row)
        csvRow = []
        for i in row.split(','):
            csvRow.append(i)
        writer.writerow(csvRow)
finally:
    csv_File.close()