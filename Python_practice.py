print("hello world")
type(3)
my_dictionary = {}
counties_dict = {}
counties_dict ["Arapahaoe"] = 422829
counties_dict
print(counties_dict)
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties[1])
counties [0]
counties[2]
print(counties[2])
counties.count
print(counties.count)
counties.append ("El Paso")
print(counties)
counties.append("Testcity")
print(counties)
print(counties)
print ("hello world")
print (counties)
print(counties[0:2])
len(counties)
counties= ['arapahoe', 'denver', 'jefferson']
print(counties)
len(counties)
counties[0:2]
counties[:3]
counties.append("El Paso")
print ('counties')
print (counties)
counties.insert(2, 'el paso')
counties.pop(3)
counties.remove('el paso')
print (counties)
counties.pop(2)
counties.insert(2, 'jefferson')
print(counties)
counties[2]= 'El Paso'
print(counties)
counties[2] = 'Jefferson'
print(counties)
counties.insert(2, "el paso")
counties.pop(1)
counties.pop(0)
counties.insert(0, 'denver')
print(counties)
counties.pop(0)
counties.insert(2, 'denver')
print(counties)
counties[2]= 'Arapahoe'
print(counties)
counties_tuple = ()
counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
print(counties_tuple)
len(counties_tuple)
counties_tuple[1]
counties_dict = dict()
counties_dict['Arapahoe'] = 422829
counties_dict
print(counties_dict)
counties_dict["Denver"]= 463353
counties_dict["Jefferson"]= 432438
print(counties_dict)
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get('Jefferson')
counties_dict.get('Arapahoe')
counties_dict['Arapahoe']
my_votes = int(300)
total_votes = int(1000)
percent_votes = (my_votes / total_votes)*100
print (percent_votes)
print (counties_dict)
print (counties_tuple)
counties = ['Arapahoe','Denver', 'Jefferson']
if counties [1] == 'Denver':
    print(counties [1]) 
temperature = int(85)
if temperature > 85:
    print("Turn on the AC")
else:
    print("open the window")
score = int(76)
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
         print ('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
score = int(86)
if score >= 90:
    print ('Your grade is an A.')
elif score >= 80:
    print ('Your grade is a B.')
elif score >= 70:
    print ('Your grade is a C.')
elif score >= 60: 
    print ('Your grade is a .')
else:
    print ('Your grade is an F.')
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties: 
    print ("El Paso is in the list of counties")
else:
    print ("El Paso is not in the list of Counties")
if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties.")
else:
    print("Araphaoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print ("Araphaoe or El Paso are in the list of counties")   
else:
    print("Arapahoe or El Paso are not in the list of counties")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Araphaoe is in the list of counties and El Paso is not in the list of counties")
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in range(5):
    print (num)
for i in range(len(counties)):
    print(counties[i])
for num in range(len(counties_tuple)):
    print(counties_tuple[i])
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for county in counties_dict.values():
    print(county)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
my_votes = int(70)
total_votes = int(1000)
percent_votes = (my_votes / total_votes) * 1000
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " +  str(voters) + " registered voters.") 
for county, voters in counties_dict.items(): 
    print(f"{county} county has {voters} registered voters")
import csv
dir(csv)