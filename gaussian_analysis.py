import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower, upper):
    if isinstance(loc , (int, float)) == True and isinstance(scale, (int, float)) == True and isinstance(lower, (int, float)) == True and isinstance(upper, (int, float)) == True:        
        if lower < upper: 
            # draw 100 samples from a gaussian distribution with loc and scale 
            gaus = np.random.normal(loc, scale, 100)
            #mask it to folter out the wrong values
            ubound = gaus < upper
            gaus = gaus[ubound]
            lbound = gaus > lower
            gaus = gaus[lbound]
            print(gaus) # print array to check 

            #calculate mean and standard deviation 
            mean = np.mean(gaus)
            std = np.std(gaus)
            t = tuple((mean, std))  #turning it into a tuple 
            print(f"the mean and standard deviation are: {t} respectively")
            return t
        else: 
            print("the lower bound must be smaller than the upper bound")
    else: 
        print("you must enter only numbers")    


if __name__ == "__main__":
    # use this for your own testing!
    gaussian_analysis(0,3,1,3)
