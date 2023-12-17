people = [ {"name":"Alice", "age":30, "occupation":"engineer"},
           {"name":"Bob", "age": 28,"occupation":"doctor"}, 
           {"name":"Charlie", "age":35, "occupation":"engineer"},
            {"name":"David", "age":22, "occupation":"doctor"},
            {"name":"Eve", "age": 29,"occupation": "artist"}]


# creating a list and appending all types of occupations available
a = []
for i in people:
    a.append(list(i.values())[2]) 

# now converting the list to set which has unique occupation types
a= set(a)

#creating a dictionary with occupation types and names of people who work in that occupation type
d = {}
for i in people:
    if i['occupation'] in a:
        b = i['occupation']
        if b not in d.keys():
            d[b]=[]
            d[b].append(i['name'])
        else:
            d[b].append(i['name'])

print(d) # printing the results  

    