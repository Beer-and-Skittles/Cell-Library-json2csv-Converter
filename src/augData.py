import numpy as np
import matplotlib.pyplot as plt

class augData:

    def __init__(self, output_loads, input_slopes, values):
        # print(values)
        assert len(values) == len(output_loads)
        assert len(values[0]) == len(input_slopes)
        assert len(output_loads) >= 2
        assert len(input_slopes) >= 2

        self.val = np.array(values).astype(np.float).tolist()
        self.opl = np.array(output_loads).astype(np.float).tolist()
        self.ins = np.array(input_slopes).astype(np.float).tolist()
    
    def augBy(self, n):
        '''
        returns data augmented by n interations;
        if n == 0, returns original data
        '''
        opl, ins, val = self.opl[:], self.ins[:], self.val[:]
        for i in range(n):
            self.augArr(opl)
            self.augArr(ins)
            self.augMat(val)
        
        return opl, ins, val

    def augArr(self, arr):
        '''
        augments list by inserting mean vals between entries
        len(n) => len(2*n-1)
        '''
        ptr = 0
        while ptr+1 < len(arr):
            avg = (arr[ptr]+arr[ptr+1])/2.0
            arr.insert(ptr+1, avg)
            ptr += 2
        return arr

    def augMat(self, mat):
        '''
        augments matrix by 
            (1) inserting mean rows between rows
            (2) inserting mean vals between entries in each rows
        shape(n by m) => shape(n*2-1 by m*2-1)
        '''
        ptr = 0
        while ptr+1 < len(mat):
            avg = ((np.asarray(mat[ptr])+np.asarray(mat[ptr+1])) / 2.0).tolist()
            mat.insert(ptr+1, avg)
            ptr += 2

        for arr in mat:
            self.augArr(arr)
        
        return mat

    def plot(self, arr1, arr2, mat):
        '''
        plots given data into a 3d plot by matplotlib
        '''
        plt.style.use('_mpl-gallery')
        X, Y, Z = [], [], []
        for i1 in range(len(mat)):
            for i2 in range(len(mat[i1])):
                X.append(arr1[i1])
                Y.append(arr2[i2])
                Z.append(mat[i1][i2])
        
        fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
        ax.scatter(X,Y,Z)

        plt.show()


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

    testClass = augData(a0, b0, v0)
    A, B, V = testClass.augBy(5)
    print(len(A), len(B), len(V), len(V[0]))



# test()

