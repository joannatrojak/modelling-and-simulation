from random import randint

def ca_data(height,width,dorandom,rulenum):
    # Create the first row, either randomly, or with a single 1
    if dorandom:
        first_row = [randint(0,1) for i in range(width)]
    else:
        first_row = [0]*width
        first_row[width//2] = 1
    results = [first_row]

    # Convert the rule number to a list of outcomes. 
    rule = [(rulenum//pow(2,i)) % 2 for i in range(8)]

    for i in range(height-1):
        data = results[-1]
        # Determine the new row based on the old data. We first make an
        #  integer out of the value of the old row and its two neighbors
        #  and then use that value to get the outcome from the table we
        #  computed earlier
        new = [rule[4*data[(j-1)%width]+2*data[j]+data[(j+1)%width]]
               for j in range(width)]
        results.append(new)
    return results
print(ca_data(10, 10, 1, 30))
