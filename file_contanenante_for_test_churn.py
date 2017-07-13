import os, glob
os.chdir('..')

os.chdir("data\\testing")
print os.getcwd()
filenames = []
for file in glob.glob('*play.log'):
	filenames.append(file)
print len(filenames)

with open('0422_0512_play_short.log', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                line = line.rstrip('\n')
            	ent = line.split('\t')
            	new_line = ent[0] + '\t' + ent[2] + '\t' + fname[:8] + '\n'
                outfile.write(new_line)