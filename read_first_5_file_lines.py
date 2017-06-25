file_name_read = '/Users/Nate/Dropbox/Research/Lehtio_Laboratory/Projects/breast_cancer/cell_lines/cell_line_encyclopedia/mRNA_microarray/CCLE_Expression_2012-09-29.res'
file_name_write = '/Users/Nate/Desktop/quantities0.txt'
i = 0
with open(file_name_read, 'r') as read_file, open(file_name_write,'w') as write_file:
    for line in read_file:
        line_split = line.split('\t')
        #del line_split[1]
        line_joined = '\t'.join(line_split)
        write_file.write(line_joined)
        i = i+1
        #if i % 100 == 0:
            #print(i)
        if i>5:
            break
