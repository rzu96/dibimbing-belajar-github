import csv
import os


file_path = r'C:\Users\redytian.zulhamsah\OneDrive - PT Gunung Raja Paksi Tbk\Documents\GITHUB\username.csv'  # Path lengkap ke file CSV


with open(file_path, 'r') as file:
    
    reader = csv.reader(file)
    
    
    for row in reader:
        print(row)
