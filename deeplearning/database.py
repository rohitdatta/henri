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