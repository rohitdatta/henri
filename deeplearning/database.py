from enum import Enum
''' generates a database for searching for salaries based on certain demographics
	output: map<role, map<company, map<state, map<city, [salary_sum, salary_count]>>>>
	input: file contain path to the file containing data
		file type: job_title\temployer_name\tworksite_state\tworksite_city\twage
'''
def gen_database(file):
	db = {}
	input_file = open(file)
	for line in input_file:
		row = line.split("\t")
		if row[0] in db:
			companies = db[row[0]]
			if row[1] in companies:
				states = companies[row[1]]
				if row[2] in states:
					cities = states[row[2]]
					if row[3] in cities:
						tup = cities[row[3]]
						total = int(tup[0]) + int(row[4])
						num = tup[1] + 1
						cities[row[3]] = (total, num)
					else:
						# add new city to the map of cities and add the wage to it
						tup = (int(row[4].rstrip('\n')), 1)
						cities[row[3]] = tup
						continue;
				else:
					# add new state to the map of states
					tup = (int(row[4].rstrip('\n')), 1)
					city = {row[3]:tup}
					states[row[2]] = city
					continue;
			else:
				# add new company name to the map of companies
				tup = (int(row[4].rstrip('\n')), 1)
				city = {row[3]:tup}
				state = {row[2]:city}
				companies[row[1]] = state
				continue;
		else:
			# add new role to map database
			tup = (int(row[4].rstrip('\n')), 1)
			city = {row[3]:tup}
			state = {row[2]:city}
			company = {row[1]:state}
			db[row[0]] = company
	return db

''' generates the dataset to be analyzed by mapping linkedin data to the h1b database
	input: name\tlinkedin\tjob_title\temployer\tstate\tcity
	output: [name, linkedin, job_title, employer, state, city, wage]
'''
def gen_dataset(file, db):
	dataset = []
	input_file = open(file)
	for line in input_file:
		row = line.split("\t")
		row[-1] = row[-1].rstrip('\n')
		if row[2] in db and row[3] in db[row[2]] and row[4] in db[row[2]][row[3]] \
		and row[5] in db[row[2]][row[3]][row[4]]:
			tup = db[row[2]][row[3]][row[4]][row[5]]
			wage = int(tup[0]) / int(tup[1])
			row.append(wage)
			dataset.append(row)
	return dataset
