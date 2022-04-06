import csv
import json


# Extract JSON Data
file_name = 'teams-location.json'
with(open(file_name, 'r') as json_file):
    data = json.load(json_file)

# Set up CSV parameters and writer``
header = ['Team Code', 'Arena', 'Latitude', 'Longitude']
file_out_name = 'teams-location.csv'
file_out = open(file_out_name, 'w')
csv_writer = csv.writer(file_out)
csv_writer.writerow(header)

# Write rows to the CSV file
for team in data.keys():
    row = [str(team), str(data[team]['arena']), data[team]['lat'], data[team]['long']]
    csv_writer.writerow(row)

file_out.close()
