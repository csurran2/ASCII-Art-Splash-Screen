import random
import os
i = random.randrange(0) + 1 
website="https://raw.githubusercontent.com/csurran2/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
