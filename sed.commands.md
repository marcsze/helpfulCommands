###Sed commands for large scale text editing

**Gets rid of the character between the / and //**

sed 's/>//' test.fasta > test2.fasta

**Gets rid of everything after "_"**

sed 's/_.*//' test2.fasta > test3.fasta

**Gets rid of everything after the first space**

sed 's/\s.*$//' test4.fasta > test5.fasta

**Gets rid of everything before "_"**

sed 's/.*_//' test2.fasta > test4.fasta

**remove all white spaces**

sed -r 's/\s+//g' list2.txt > list3.txt

**add something to the end of every word on the line (in this case the *)**

sed 's/\>/*/g;s/*$//' list4.txt > list5.txt

**add to the end of every line**
**($ represents end, word between 2nd and 3rd / is what is added)**

sed 's/$/.fasta/' name2.txt > name3.txt

**add to the beginning of every line (^ is beginning 2nd and 3rd / is what is added)**

sed 's/^/> /' name3.txt > name4.txt

**Remove something after a period**

sed 's/\..*$//' names.txt > names2.txt

**Replace a word with another word**

sed 's/old/new/g' test.txt > test2.txt

**Remove a space at the beginning of every line**

sed 's/[ \t]*\(.*\)/\1/' input.txt >output.txt

**Delete every 2nd line**

sed -n "p;N;" input.txt > output.txt




