import csv
with open("csv1.csv",mode="r+",newline='') as csvfile:
    data=csv.DictReader(csvfile)
    header=next(data)
    #for row in data:
        #print(row)
    writing=csv.writer(csvfile)
    i=[11,12,13]    
    writing.writerow(i)
    for row in data:
        print(row)