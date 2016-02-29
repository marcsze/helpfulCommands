###Other useful commands for large scale text editing

**Remove columns (3 specifes 3rd column onwards keep)**

cut -d " " -f 3- input.file > output.file

**remove double spaces with a single spaces**

tr -s " " < combined > test

**Rename multiple files in bulk**

rename 'xyz.file' 'xyz123.file' *file

**Combine the two files together in a column format (\t stands for tab)**

paste -d"\t" test5.fasta test3.fasta > test.groups

**Keeps anything with ">" in it**

grep -e '^>' V2.fasta > test.fasta

**Convert files from windows to linux on the command line**

awk '{ sub("\r$", ""); print }' winfile.txt > unixfile.txt

**and vice versa**

awk 'sub("$", "\r")' unixfile.txt > winfile.txt

**Generate list of two columns that is not common to both files**

comm -1 -3 what.you.don't.want.txt full.list.txt > output.txt

**combine two files (first file, second file, ...nfile)**

cat file1 file2 > output.file

**Find common names in two files**

grep -f file1.csv file2.csv > common.csv


**Output a text file with two columns when compared to a text file with only one column** 
**(outputs two columns of what was not common between the two text files)**

awk '
FNR==NR {                     
data [ $1 ] = 1;
next;
}
FNR < NR {
if ( ! ($1 in data) ) {
print $0;
}
}
' test1.1.groups trial1.groups > new.groups

**Compare two files and output what is not in first file**
**(not in file 1 '^>' not in file 2 '^<')**

diff file1-sorted.txt file2-sorted.txt | grep '^>' not-in-file1.txt

**Sort files** 

sort file1.txt > file1-sorted.txt; sort file2.txt > file2-sorted.txt

**removing selective parts from text file title (output name: abcd_b_c)**

gawk -F "_" '/^[^>]/{print;next};{a=$1;b=$2;c=$3;print a "_" b "_" c}' < input.fasta > output.fasta

**removing parts from text file and replacing with just the first part name before "_"** 
**(output name: abcd)**

gawk -F "_" '/^[^>]/{print;next};{a=$1;print a}' < input.fasta > output.fasta











