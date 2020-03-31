import pandas as pd
#file_csv = pd.read_csv('cars.csv',delimiter= ';',nrows=3,skiprows=3 )
#file_csv = pd.read_csv('cars.csv',delimiter= ';',usecols=[0,2,3,5] )
#file_csv_no_header = pd.read_csv('cars.csv',delimiter= ';',header=None )
file_csv_no_header = pd.read_csv('cars.csv',delimiter= ';',header='infer' )



print(file_csv_no_header.columns)
print(file_csv_no_header.dtypes)

print(file_csv_no_header.head()) 
 
#print(file_csv.head(2)) 
#print(file_csv) 

#remote_file = 'https://raw.githubusercontent.com/aranda-labs/VisorLogs/master/logs/ArandaConserver2.csv'

#remotecsv = pd.read_csv(remote_file)

#print(remotecsv.head(2)) 