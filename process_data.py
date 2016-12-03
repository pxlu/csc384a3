import a3_classes as a3c
import csv

def main():

	inputs_path = "data.csv"
	with open(inputs_path, 'r') as csvfile:
		data_reader = csv.DictReader(csvfile)
		data_list = [a3c.ItemProfile(name=row['Name'],price=row['Price'],brand=row['Brand'],seasonal=row['Seasonal'] if row['Seasonal'] != '' else 'Any',category=row['Categories'],is_entertainment=row['Entertainment?'],is_indoor=row['Indoor?'],rec_age=row['Recommended Age'] if row['Recommended Age'] != '' else '0+') for row in data_reader]

	for data in data_list:
		print(str(data))

if __name__ == "__main__":
	main()