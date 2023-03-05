import numpy as np

def augment(values, output_loads, input_slopes):
    val_sorted = np.asarray(values).reshape(len(output_loads),len(input_slopes))
    output = []

    # place original values into output
    for i in range(len(output_loads)):
        for j in range(len(input_slopes)):
            output.append([val_sorted[i][j], input_slopes[j],output_loads[i]])
    
    # augmented output_loads and input_slopes axes
    aug_ol, aug_is = [], []
    for i in range(1,len(output_loads)):
        aug_ol.append((output_loads[i]+output_loads[i-1])/(2.0))
    for i in range(1,len(input_slopes)):
        aug_is.append((input_slopes[i]+input_slopes[i-1])/(2.0))
    
    # augmented output_loads and original input_slopes
    for i in range(len(aug_ol)):
        for j in range(len(input_slopes)):
            val = (val_sorted[i][j] + val_sorted[i+1][j])/2.0
            output.append([val, input_slopes[j], aug_ol[i]])

    # original output_loads and augmented input_slopes
    for i in range(len(output_loads)):
        for j in range(len(aug_is)):
            val = (val_sorted[i][j] + val_sorted[i][j+1])/2.0
            output.append([val, aug_is[j], output_loads[i]])

    # augmented output_loads and augmented input_slopes
    for i in range(1, len(output_loads)):
        for j in range(1, len(input_slopes)):
            val = (val_sorted[i][j] + val_sorted[i-1][j-1])/2.0
          
    return output

def testing():
    a = [0.016, 0.032, 0.064, 0.128, 0.256, 0.512, 1.024]
    b = [0.1, 0.25, 0.5, 1, 2, 4, 8]
    v = [[0.0222266,0.0233764,	0.0232818,	0.0196093,	0.0085917,	-0.0180836,	-0.0740405],\
        [0.022946,	0.024124,	0.0240854,	0.0205322,	0.0096225,	-0.0169005,	-0.0727904],\
        [0.0240977,	0.0253166,	0.0253586,	0.0220022,	0.0112925,	-0.0149723,	-0.0706302],\
        [0.026258,	0.0275274,	0.0276999,	0.0247356,	0.0143809,	-0.0111995,	-0.0658622],\
        [0.030232,	0.0315794,	0.0320106,	0.0296332,	0.0202829,	-0.0042705,	-0.058073],\
        [0.037464,	0.0388656,	0.039508,	0.0381538,	0.0304244,	0.0086323,	-0.0435077],\
        [0.0508379,	0.0522553,	0.0532982,	0.0530272,	0.0479443,	0.0297155,	-0.0172538]]
    output = augment(v,a,b)
    print('new len is:',len(output))


# testing()

