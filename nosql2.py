#import pymongo
#from pymongo import MongoClient
# client = MongoClient()

import re
def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://Yan294:UabDBDJp4dxwF8r@cluster0.vevkc.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    # Create the database
    return client.nosql2#client['nosql1']
    
if __name__ == "__main__":        
    # Get the database
    dbname = get_database()

collection_name = dbname

continents = collection_name.continents
countries = collection_name.countries
#print(collection_name.list_collection_names())


#QUESTION 1
print("Q1 - Get all countries which have given string in name\n")
country_str = str(input("Enter word matching the country\n"))
for x in countries.find({ "Name": re.compile(country_str, re.IGNORECASE)}):
    print(x)
print("\n\n")


#QUESTION 3
print("Q3 - List of continents with number of countries\n")
for i in continents.find({}):    
    print(i['Name'],i['countries'].count(",")+1)
print("\n\n")


#QUESTION 4
print("Q4 - Get first4 countries in alphabeti\n")
four = countries.find({},{'Name':1, 'countries':{'$slice':2}}).sort("Name")#"continents":["621b6e480f1e033fc8c06c4d"]
for i in four:
    print(i)
print("\n\n")

#QUESTION 5

countries.update_one({'Name': 'USA'}, {'$set': {'Population': 332915073}})
countries.update_one({'Name': 'Australia'}, {'$set': {'Population':25987867}})
countries.update_one({'Name': 'Morocco'}, {'$set': {'Population': 37632126}})
countries.update_one({'Name': 'India'}, {'$set': {'Population': 1402420930}})
countries.update_one({'Name': 'UK'}, {'$set': {'Population': 67081000}})
countries.update_one({'Name': 'Mexico'}, {'$set': {'Population': 126014024}})
countries.update_one({'Name': 'Egypt'}, {'$set': {'Population': 102674145}})
countries.update_one({'Name': 'China'}, {'$set': {'Population': 14485086609}})
countries.update_one({'Name': 'France'}, {'$set': {'Population': 65512203 }})
countries.update_one({'Name': 'Italy'}, {'$set': {'Population': 60317116}})

#QUESTION 6
print("Q6 - All countries sorted by number of people\n")
pop = countries.find({}).sort("Population")
for i in pop:
    print(i['Name'],i['Population'])
print("\n\n")

#QUESTION 7
print("Q7 - Countries with a 'u' in name and more than 100 000 people\n")
for x in countries.find({ "Name": re.compile("u", re.IGNORECASE), 'Population': {'$gt': 100000}}).sort("Population"):
    print( x['Name'], x['Population'])
