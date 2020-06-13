import csv
import re

#Fucntion to add . in mac address to get the default AP name
def f_dot(my_str, group=4, char='.'):
     my_str = str(my_str)
     return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

# Fucntion to clean the mac address to a consistent format
def f_clean_mac_format(my_str):
     my_str = str(my_str)
     my_str = re.sub('[:.-]', '', my_str)
     return my_str

def f_add_quotes(my_str):
     str2 = '"'
     my_str = str(my_str)     	 
     return str2+my_str+str2

with open('Input.csv') as f:
    reader = csv.reader(f)
    with open('output.txt', 'w') as g:
        writer = csv.writer(g)
        # Skip the header
        next(reader)
        for row in reader:            
            print ("ap name AP" + f_dot(f_clean_mac_format(row[1]))+ " name " + row[0])
            new_row = ["cli.executep(" + "ap name AP" + f_dot(f_clean_mac_format(row[1]))+ " name " + row[0] + ")"]
            writer.writerow(new_row)
            print("ap name " + row[0] + " location " +  f_add_quotes(row[2]))
            new_row = ["cli.executep(" + "ap name " + row[0] + " location " +  f_add_quotes(row[2]) +  ')']
            writer.writerow(new_row)

