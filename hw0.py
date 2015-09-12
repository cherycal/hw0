myfile = open('iowa-liquor-sample.csv','r');
sum = 0

for line in myfile:
    if 'single malt scotch' in line.lower():
        sum+=1

print("Sum: " + str(sum))

