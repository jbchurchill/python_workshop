from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

outFile = open ('output_result.txt', 'w')
outFile.write("")

filenames = find_csv_filenames('./')
for curFile in filenames:
  file = open(curFile, 'r')
  n=0
  for i, line in enumerate(file):
    if (not n == 0):
      #print line
      outFile.write(line)
    #print n
    n+=1
  file.close()
outFile.close()