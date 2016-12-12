import sys


print ("Hello, Python!");

days = ['Monday', 'Tuesday']

paragraph = """This is a test paragraph. I want to see if you can keep going with it."""
item_one = "testing one "
item_two = "testing two "
item_three = "testing three"
a = 5
b = 20
numList = [1,2,3,4,5]
testList = ['brian','getz','program','python','test']
testTuple = ('brian','getz','program','python','test')
newDict = {}
newDict['one'] = "This is my first one"
newDict[2] = "Another example"
combinedDict = {'name':'Brian Getz','occupation:':'Developer','age':'27'}
var = 100
numListIt = iter(numList) #Builds an iteration object




total = item_one + \
    item_two + \
    item_three

print (paragraph[2:10]) #Paragraph
print (testList[0:3]) #List are editable
print (testTuple[0:3]) #Tuple are not editable
print (newDict['one'])
print (newDict[2])
print (combinedDict)
print (combinedDict.keys())
print (combinedDict.values())

if (a in numList):
    print ("Line 1 - a is available in given list")
else:
    print ("Line 1 - a is not available in given list")

if (var == 100) : print ("Value of expression is 100")


print (next(numListIt))


for x in numListIt:
    print (x, end="\n")

#while True:
#    try:
#        print (next(numListIt))
#    except StopIteration:
#        sys.exit()


print ("My name is %s and weight is %d lbs" % ('Brian', 200))