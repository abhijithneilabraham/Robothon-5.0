import csv

Coor=[]
with open('GPSValues.csv', 'w') as csvfile:
    fieldnames = ['Latitude', 'Longotude']
 
        
          
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer = csv.writer(csvfile)
    X=9.3172012081
    Y=76.6780318411
    for i in range(0,100):
        Coor.append(X+(0.0000000001*((i*23)%7)))
        Coor.append(Y+(0.0000000001*((i*29)%7)))

        
        
    writer.writerow(Coor)
