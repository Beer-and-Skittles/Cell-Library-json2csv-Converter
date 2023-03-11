import numpy as np

class augData:

    def __init__(self, values, output_loads, input_slopes):

        assert len(values) == len(output_loads)
        assert len(values[0]) == len(input_slopes)
        assert len(output_loads) >= 2
        assert len(input_slopes) >= 2

        self.val = values
        self.opl = output_loads
        self.ins = input_slopes
    
    def augBy(self, n):
        for i in range(n):
            self.augArr(self.opl)
            self.augArr(self.ins)
            self.augMat(self.val)
            print(len(self.opl), len(self.ins), len(self.val))

    def augArr(self, arr):
        ptr = 0
        while ptr+1 < len(arr):
            avg = (arr[ptr]+arr[ptr+1])/2.0
            arr.insert(ptr+1, avg)
            ptr += 2
        return arr

    def augMat(self, mat):
        ptr = 0
        while ptr+1 < len(mat):
            avg = ((np.asarray(mat[ptr])+np.asarray(mat[ptr+1])) / 2.0).tolist()
            mat.insert(ptr+1, avg)
            ptr += 2

        for arr in mat:
            self.augArr(arr)
        
        return mat

def test():
    a0 = [0.016, 0.032, 0.064, 0.128, 0.256, 0.512, 1.024]
    b0 = [0.1, 0.25, 0.5, 1, 2, 4, 8]
    v0 = [[0.0222266,0.0233764,	0.0232818,	0.0196093,	0.0085917,	-0.0180836,	-0.0740405],\
        [0.022946,	0.024124,	0.0240854,	0.0205322,	0.0096225,	-0.0169005,	-0.0727904],\
        [0.0240977,	0.0253166,	0.0253586,	0.0220022,	0.0112925,	-0.0149723,	-0.0706302],\
        [0.026258,	0.0275274,	0.0276999,	0.0247356,	0.0143809,	-0.0111995,	-0.0658622],\
        [0.030232,	0.0315794,	0.0320106,	0.0296332,	0.0202829,	-0.0042705,	-0.058073],\
        [0.037464,	0.0388656,	0.039508,	0.0381538,	0.0304244,	0.0086323,	-0.0435077],\
        [0.0508379,	0.0522553,	0.0532982,	0.0530272,	0.0479443,	0.0297155,	-0.0172538]]
    
    a1 = [0,2,4]
    b1 = [1,3,5,7]
    v1 = [[0,4,8,12],\
          [16,20,24,28],\
          [32,36,40,44],]

    testClass = augData(v1, a1, b1)
    testClass.augBy(5)


test()

