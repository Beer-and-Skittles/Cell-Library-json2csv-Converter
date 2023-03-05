import numpy as np

def augment(output_loads, input_slopes, values):
    val_sorted = np.asarray(values).reshape(len(output_loads),len(input_slopes))
    # print('before',val_sorted)
    outTable = {}

    # place original values into outTable
    for i in range(len(output_loads)):
        for j in range(len(input_slopes)):
            # print(val_sorted[i][j], input_slopes[j], output_loads[i])
            outTable[val_sorted[i][j]] = [input_slopes[j],output_loads[i]]
    
    # augmented output_loads and input_slopes axes
    aug_ol, aug_is = [], []
    for i in range(1,len(output_loads)):
        aug_ol.append((output_loads[i]+output_loads[i-1])/(2.0))
    for i in range(1,len(input_slopes)):
        aug_is.append((input_slopes[i]+input_slopes[i-1])/(2.0))
    
    print('before', len(outTable))
    
    # augmented output_loads and original input_slopes
    for i in range(len(aug_ol)):
        for j in range(len(input_slopes)):
            val = (val_sorted[i][j] + val_sorted[i+1][j])/2.0
            outTable[val] = [input_slopes[j], aug_ol[i]]

    # original output_loads and augmented input_slopes
    for i in range(len(output_loads)):
        for j in range(len(aug_is)):
            val = (val_sorted[i][j] + val_sorted[i][j+1])/2.0
            outTable[val] = [aug_is[j], output_loads[i]]

    # augmented output_loads and augmented input_slopes
    for i in range(1, len(output_loads)):
        for j in range(1, len(input_slopes)):
            val = (val_sorted[i][j] + val_sorted[i-1][j-1])/2.0
            outTable[val] = [aug_is[i-1], aug_ol[j-1]]

    print('done', len(outTable))

a = [0,0.1,0.2,0.3,0.4]
b = [10,20,30,40,50]
v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
augment(a,b,v)