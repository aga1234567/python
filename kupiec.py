import numpy as np


"""for i in range(1,40):
    s=i*0.5
    if((2*(2*(2*s-12)-12)-12)==0):
        print(s)"""

for i in np.arange(1,20,0.5):
 if ((2 * (2 * (2 * i - 12) - 12) - 12) == 0):
  print(round(i,2))


