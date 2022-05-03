import sys


f = open(sys.argv[1])

for line in f:
    orig_line = line

    # comment_pos = line.find('#')
    # if comment_pos != -1:
    #     line = line[:comment_pos]
    
    # if line.isspace():
    #     continue
    
    fields = line.split('#')
    if fields[0].isspace():
        continue

    print(orig_line, end='')



    
