import os

for curdic, direcs, files in os.walk("/Users/archys/projects/data_algorithm"):
    print(curdic)
    print(direcs)
    print(files)
