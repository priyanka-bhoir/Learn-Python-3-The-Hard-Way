# stuff={'name':'priyanka','age':20,'height':6*12+2}
# print(stuff['name'])
# print(stuff['age'])
# print(stuff['height'])
# stuff['city']="SF"
# print(stuff['city'])
# print(stuff)
#create a mapping of stste to abbriviation
states={
	'Oregon':'OR',
	'Florida':'FL',
	'Califonia':'CA',
	'New york':'NY',
	'Michigan':'MI'
}
#create a basic set and some cities in them
cities={
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'JAcksonville'
}
print(cities.get('FL'))

#add some more cities
cities['NY']='New york'
cities['OR']='Portland'
#print out some cities
print('-'*10)
print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

#print some states
print("-"*10)
print("Michigan's abbriviation is:",states['Michigan'])
print("Florida's abbriviation is:",states['Florida'])

#do it by using the states then cities dict
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbrivation
print('-'*10)
for state,abbr in list(states.items()):
	print(f"{state} state is abbrivated {abbr}")
	print(f"and has city {cities[abbr]}")

print("-"*10)
for abbr,city in list(cities.items()):
	print(f"{abbr} has the city {city}")

#now do both at the same time 
print('-'*10)
for state,abbrv in list(states.items()):
	print(f"{state} state is abbrivated {abbrv}")
	print(f"and has city {cities[abbrv]}")

print('-'*10)
#safely get a abbreviation by state that might not be there
state=states.get("Texas")

if not state:
	print("Sorry, no Texas.")

#get a city with a default value
city=cities.get('TX','Does not Exit')
print(f"The city for the state 'TX' is:{city}")



