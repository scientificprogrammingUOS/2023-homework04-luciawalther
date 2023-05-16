import numpy as np

# implement the function strange pattern
def strange_pattern(m):
    #creates a numpy array 2D filled with zeros and of type bool, so 0 = False 
    
    arr = np.zeros(m, dtype = "bool")
    #create the pattern -> [outer dimension start:stop:step, inner dimension start:stop:step] and turn True 
    arr[::3, ::3] = True
    arr[1::3, 2::3] = True
    arr[2::3, 1::3] = True
    return arr

if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern((5,6)))



