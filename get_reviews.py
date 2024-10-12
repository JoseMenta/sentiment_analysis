import csv
import json
import requests
import os

r = requests.get('https://www.rottentomatoes.com/napi/movie/24287464-bfdc-362a-b386-aa62895c2a1b/reviews/verified_audience?after=eyJyZWFsbV91c2VySWQiOiJGYW5kYW5nb18xOTkyMzRCNy02QjA4LTQ4NDQtOTg3Ny04MTQ0NzdGMDVCN0MiLCJlbXNJZCI6IjI0Mjg3NDY0LWJmZGMtMzYyYS1iMzg2LWFhNjI4OTVjMmExYiIsImVtc0lkX2hhc1Jldmlld0lzVmlzaWJsZUlzVmVyaWZpZWQiOiIyNDI4NzQ2NC1iZmRjLTM2MmEtYjM4Ni1hYTYyODk1YzJhMWJfVCIsImNyZWF0ZURhdGUiOiIyMDI0LTEwLTA2VDA3OjMwOjQ2LjUwMloifQ%3D%3D&pageCount=150')
data = json.loads(r.text)
reviews = data['reviews']
# File path for the CSV file
csv_file_path = 'data/reviews.csv'

os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    writer.writerow(['review'])
    # Write data to the CSV file
    for review in reviews:
        try:
            writer.writerow([review['quote']])
        except:
            pass