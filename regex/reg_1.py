import re 

#1 if re.search("inform", "we need to inform him the latest information"):
#     print("There is inform")

#2 allinform = re.fandall('inform', "we need to inform him the latest information")

# for x in allinform:

#     print(i)

# str = "we need to inform him the latest information"

#3 for x in re.finditer("inform",str):
#     loctup = x.span()
#     print(loctup)

#4 str = "Sat, mat, hat, pat"

# allstr = re.findall("[Sshmp]at", str)

# for x in allstr:
#     print(x)

#5 str = "Sat, mat, hat, pat"

# allstr = re.findall("[h-z]at", str)

# for x in allstr:
#     print(x)

#6 allstr = re.findall("[^h-z]at", str) #everything apart [h-z]

# for x in allstr:
#     print(x)

#7 
# food = 'hat rat mat pat'

# regex = re.compile('[p]at')

# food = regex.sub("food", food)

# print(food)

# randstr = '''
# Keep the blie flag
# flying high
# Chelsea
# '''
# regex = re.compile('\n')

# randstr = regex.sub(' ', randstr)

# print(randstr)

# print()

#9 randstr = '123457'

# print ("Matches: ", len(re.findall("\d", randstr)))

# \w [a-zA-z0-9_]
# \W [^a-zA-Z0-9]

# phone = "233-333-43535"

# if re.search("\w{3}-\w{3}-\w{4}", phone):
#     print("it is a phone number")

#if re.search("\w{0,4}\s\w(0,4)", "sdsd sddd"):
    # print("valid")
