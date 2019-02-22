import csv

    
with open('values.csv', 'w') as csvfile:
    fieldnames = ['temperature', 'humidity']
 
        
          
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
        dic={'temperature':temp,'humidity': hum}
        
        
        writer.writerow(dic)
