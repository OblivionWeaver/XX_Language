import sys,os
import numpy as np
name = 'Cpp'
ext = '.cpp'
bite = 50000000
def main():
    with open(name+ext,"wb") as file:
        file.write(np.random.bytes(bite))
   
    return 0

if __name__ == "__main__":
    main()