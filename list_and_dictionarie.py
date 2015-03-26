zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

#Slicing Lists and Strings
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
print cat
dog  = animals[3:6]  # The fourth through sixth characters
print dog
frog = animals[6:]  # From the seventh character to the end
print frog