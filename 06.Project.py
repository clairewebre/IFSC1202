Input = open("06.Project Input File.txt","r") #opens input file
Output = open("06.Project Output File.txt", "w") #opens output file
InputRecord = 0
OutputRecord = 0
MergeRecord = 0
line = Input.readline() #reads input file
while line != "": #allows input file to be read until empty line
    if line == "**Insert Merge File Here**\n": #calls out the break in input file
        MergeFile = open("06.Project Merge File.txt", "r") #opens merge file
        Merge = MergeFile.readline() #reads merge file
        while Merge != "": #allows merge file to be read until empty line
            Output.write(Merge) #copies merge file into output file
            OutputRecord += 1 #adds 1 to output record for each line recorded from merge file
            Merge = MergeFile.readline() #reads merge file again
            MergeRecord += 1 #adds 1 to merge record for each line in merge file
        Output.write("\n") #creates a new line after inserted merge file text
        MergeFile.close() #closes merge file
    else:
        Output.write(line) #copies input text into output file
        OutputRecord +=1 #adds 1 to output record for each line copied from input file
        InputRecord +=1 #adds 1 to input record for each line in input record
    line = Input.readline() #reads input file
Input.close() #closes input file
Output.close() #closes output file
print(InputRecord, "input file record")
print(MergeRecord, "merge file record")
print(OutputRecord, "output file record")