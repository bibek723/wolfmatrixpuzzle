import  csv
file = open('csv-sample.csv')
read = csv.reader(file)
line = len(list(read))
print(line)
