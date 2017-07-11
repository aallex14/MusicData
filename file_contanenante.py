import os, glob
os.chdir('..')

os.chdir("data\\training")
print os.getcwd()
filenames = []
for file in glob.glob('*play.log'):
	filenames.append(file)
print filenames, len(filenames)

with open('0330_0421_play.log', 'w') as outfile:
    for fname in filenames[:10]:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)