#A list of names with possible duplicate entries,is given.
#Find the unique names and the number of times each name appears in the list.

#"Amal" , "Kamal" , "Sunil", "Saman", "Amal" , "Amal", "Saman" , "Nimal","Kamal". "Ajith",
#"Kamal" , "Saman", "Nismal", "Kamal", "Sunil", "Sarath"

names = ["Amal" , "Kamal" , "Sunil", "Saman", "Amal" , "Amal", "Saman" , "Nimal","Kamal","Ajith","Kamal" , "Saman", "Nimal", "Kamal", "Sunil", "Sarath"]
count = dict()#count is dictionary

for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1#count repeat name

print(count)#print dict
