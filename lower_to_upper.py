# Script to convert comma separated file to tab delimited file

lower_file = 'rna_seq_supplemental_tab_1.txt'
upper_file = lower_file[:-4] + "_upper" + '.txt'

with open(lower_file,'r') as file_read:
    with open(upper_file,'w') as file_write:
        for line in file_read:
            newline = line.upper()
            file_write.write(newline)
