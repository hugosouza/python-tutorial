#!/usr/bin/python

# x = int(raw_input("Please enter an integer:"))

x = 10
 
if x < 0:
    x = 0
    print 'Negative zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'One'
else:  
    print 'More'

a = ["test 1111", "test 2", "test 3333", "test 4"]
for y in a:
    print y, len(y)

for y in a[:]:
    if len(y) > 7: a.append(y)

print a

for y in range(10):
    print y

i = 0
for y in range(11):
    if i > 4:
        continue
    if y % 2 == 0:
        print y," ",
        i += 1
else:
    print "end"


