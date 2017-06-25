import re
import pdb
file_name_read = '/Users/Nate/Dropbox/Research/Lehtio_Laboratory/Projects/breast_cancer/cell_lines/cell_line_encyclopedia/mRNA_microarray/CCLE_Expression_2012-09-29.res'
file_name_write = '/Users/Nate/Desktop/breast_cells.txt'
i = 0
with open(file_name_read, 'r') as read_file, open(file_name_write,'w') as write_file:
    for line in read_file:
        i=i+1
        if i==1:
            line_split = line.split('\t')
            breast_cells = ['cell_line']
            breast_cell_indices = [0]
            for j in range(len(line_split)):
                item = line_split[j]
                if re.search('BREAST$',item):
                    breast_cells.append(line_split[j])
                    breast_cell_indices.append(j)
            line_joined = '\t'.join(breast_cells)
            line_joined = line_joined + '\n'
            write_file.write(line_joined)

        if i>3:
            line_split = line.split('\t')
            breast_cell_items = [line_split[k] for k in breast_cell_indices]
            line_joined = '\t'.join(breast_cell_items)
            line_joined = line_joined + '\n'
            write_file.write(line_joined)

        #if i>10:
        #    break
print('lines = ',i)
