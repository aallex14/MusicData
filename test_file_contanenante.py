import os, glob
os.chdir('..')

os.chdir("data\\testing")
print os.getcwd()
filenames = []
for file in glob.glob('*play.log'):
	filenames.append(file)
print len(filenames)

with open('0422_0512_play.log', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)