# Health Centre,Municipal Hospital,CHPS,Maternity Home,District Hospital,Regional Hospital

disease_facility = dict()

types = ["Health Centre","Municipal Hospital","CHPS","Maternity Home","District Hospital","Regional Hospital"]

facilities_file = open("health-facilities-gh.csv", "r")

facilities = facilities_file.readlines()

for facility in facilities:
	fac_type = facility.split(",")[3].strip()
	fac_name = facility.split(",")[2].strip()

	if fac_type in types:
		i = types.index(fac_type)
	else:
		continue
	
	diseases = open("health_facilities_and_diseases.csv", "r")
	for disease in diseases.readlines():
		if fac_name in disease_facility:
			val = disease_facility.get(fac_name)
			
			if disease.split(",")[i].strip() in (None, "") or val in (None, ""):
				continue
			val.extend([disease.split(",")[i].strip().lower()])
		
			disease_facility[fac_name] = val
		else:
			if disease.split(",")[i].strip() in (None, ""):
				continue
			disease_facility[fac_name] = [disease.split(",")[i].strip().lower()]
	diseases.close()
	

