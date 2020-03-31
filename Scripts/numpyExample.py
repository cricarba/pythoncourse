import numpy as np

sample = np.loadtxt('numpyFile.txt')
print(sample)
print(sample.size)
print(sample.shape)

sampleTwo = np.loadtxt('numpyFile.txt', usecols=(0,2), skiprows=1)
print(sampleTwo)
print(sampleTwo.size)
print(sampleTwo.shape)

def increase(id):
    return int(id) * 3

sampleTree = np.loadtxt('numpyFile.txt', converters={0 : increase})
print(sampleTree)
print(sampleTree.size)
print(sampleTree.shape)