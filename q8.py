# import os

# moudleList = [os.system("pip list")]

# for i in moudleList:
#     print(i)

import pkg_resources

plist = pkg_resources.working_set

for i in plist:
    print(i)