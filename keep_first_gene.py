import pdb
file_name_read = '/Users/nate/Dropbox/Research/Vacanti_Laboratory/projects/Joeva/proteomics/protein_2pepmatches_quantities/quantities.txt'
file_name_write = '/Users/nate/Dropbox/Research/Vacanti_Laboratory/projects/Joeva/proteomics/protein_2pepmatches_quantities/quantities0.txt'
i = 0
with open(file_name_read, 'r') as read_file, open(file_name_write,'w') as write_file:
    gene_list = []
    for line in read_file:
        line_split = line.split('\t')
        continue_statement = False
        #look for any missing values
        for item in line_split:
            if item == '':
                continue_statement = True
                #if a missing value is found in the line, there is no need to search anymore because the whole line is disgarded
                break
        #do not finish processing this line and move on in the loop if a missing value was found
        if continue_statement:
            continue
        gene = line_split[0]
        #remove extra gene names which are separated by a semicolon
        sep_char = ';'
        gene_split = gene.split(sep_char, 1)[0]
        gene_list.append(gene_split)
        line_split[0] = gene_split
        line_joined = '\t'.join(line_split)
        write_file.write(line_joined)
        i = i+1
        #if i % 100 == 0:
            #print(i)
        #if i>30:
        #    break
