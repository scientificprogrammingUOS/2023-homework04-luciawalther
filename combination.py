import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis = 0):
    arr1 = arr1.squeeze()
    arr2 = arr2.squeeze()
    combined = True
    arr1_shape = arr1.shape
    arr2_shape = arr2.shape

    if len(arr1_shape) == len(arr2_shape):
        for el in range(len(arr2_shape)):
            if el != axis and arr1_shape[el] != arr2_shape[el]:
                combined = False
        if combined == True:
            comb_arr = np.concatenate((arr1, arr2), axis)
            return comb_arr
        else:
            raise ValueError("These two arrays cannot be combined")
    else: 
        raise ValueError("These 2 array cannot be combined")


if __name__ == "__main__":
    # use this for your own testing!

    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,2))
    print(combination(a,b))
