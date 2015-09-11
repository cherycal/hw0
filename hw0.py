myfile = open('iowa-liquor-sample.csv','r');
sum = 0

for line in myfile:
    lowline = line.lower()
    if 'single malt scotch' in lowline:
        sum+=1

print("Sum: " + str(sum))

