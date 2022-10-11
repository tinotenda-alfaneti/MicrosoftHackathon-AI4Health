"""
{"intents": [{"Symptoms": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
         "Disease": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]}]}
"""

import json

data_set = dict()
data_list = list()

with open("dataset.csv") as data_file:
	for line in data_file:

		temp_dict = dict()
		# skip first line
		if "Disease" in line:
			continue

		line_arr = line.split(",")
		temp = []
		key = line_arr[0].lower()
		for col in line_arr[1:]:

			#skip empty spaces
			if col not in ("", "\n") :
				temp.append(col.lower().replace("_", " "))

		# add the values to a dictionary
		temp_dict["Disease"] = key
		temp_dict["Symptoms"] = temp

		data_list.append(temp_dict)
data_set["DiseaseSymptom"] = data_list
#create a json object
json_object = json.loads(json.dumps(data_set))
json_file = open("dataset.json", "w")
json_file.write(str(json_object))