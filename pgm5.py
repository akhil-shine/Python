import csv
c_col=('ID','Name','Age')
dict_data=[{'ID':1,'Name':'Abbas','Age':19},
          {'ID':2,'Name':'Akash','Age':99},
          {'ID':3,'Name':'Akhil','Age':22},
          {'ID':4,'Name':'Akku','Age':29},
          {'ID':5,'Name':'Akhila','Age':39},
          {'ID':6,'Name':'Alfu','Age':89},
          {'ID':7,'Name':'Bens','Age':14},
          {'ID':8,'Name':'Bkhil','Age':12},
          {'ID':9,'Name':'Mkku','Age':66},
          {'ID':10,'Name':'Pkhila','Age':39}]
try:
        with open("name.csv","w")as f:
                write=csv.DictWriter(f,fieldnames=c_col)
                write.writeheader()
                for i in dict_data:
                        write.writerow(i)
except IOError:
        print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in d:
    print(i)