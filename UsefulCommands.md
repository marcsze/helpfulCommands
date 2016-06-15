####Login command:
ssh -l msze compute01 -X

####Upload file:
scp file.txt msze@compute01:/home/msze/data/

####Upload file to second server 
scp -r Hogg_Run505 msze@compute01:/home/msze/data/

####Download file:
scp msze@compute01:/home/msze/data/file.txt .

####Print working directory:
pwd

####Change Directory:
cd

IP Address for Original RDP upload:

10.0.16.23

####Install rpm package:

sudo rpm -ivh packagename.rpm

####Install tar file:

tar –xvzf Apackage.tar.gz
cd Apackage
./configure
make
make install 

####directory size:
du -h

####removing selective parts from text file title (output name: abcd_b_c)

gawk -F "_" '/^[^>]/{print;next};{a=$1;b=$2;c=$3;print a "_" b "_" c}' < input.fasta > output.fasta

####removing parts from text file and replacing with just the first part name before "_" (output name: abcd)

gawk -F "_" '/^[^>]/{print;next};{a=$1;print a}' < input.fasta > output.fasta

####Delete every 2nd line:

sed -n "p;N;" input.txt > output.txt

####Remove a specific character (e.g. ">") from every line:

sed 's/>//' input.txt > output.txt

####Remove a space at the beginning of every line:

sed 's/[ \t]*\(.*\)/\1/' input.txt >output.txt

####Compare two files and output what is not in first file:
(not in file 1 '^>' not in file 2 '^<')

sort file1.txt > file1-sorted.txt; sort file2.txt > file2-sorted.txt
diff file1-sorted.txt file2-sorted.txt | grep '^>' not-in-file1.txt

####Output a text file with two columns when compared to a text file with only one column (outputs two columns of what was not common between the two text files)

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

####Generate list of two columns that is not common to both files:

comm -1 -3 what.you.don't.want.txt full.list.txt > output.txt

####combine two files (first file, second file, ...nfile)

cat file1 file2 > output.file

####Find common names in two files:

grep -f file1.csv file2.csv > common.csv

####unzip whole file to particular directory:

unzip -j filename.zip
tar zxvf fileNameHere.tgz
gzip -d file.gz
gunzip file.gz
	###un-gzip all files in a directory
		gunzip *.fastq.gz
		
bzip2 -d filename.bz2

#### Kill a screen session:

screen -S ##### -X quit

#### Adding a new PATH to commands:
(Has to be in parent directory to set it up)
PATH=$PATH:/home/msze/data/bowtie2/bowtie2-2.1.0/bowtie2-build/:home/msze/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:; export PATH

#### Link (Soft) command/program with bin folder - to allow PATH function to search bin for command and not have to retype PATH every login

ln -s /home/msze/data/bowtie2-build /home/msze/bin/bowtie2-build

#### Remove a directory

rm -r example

#### Server/computer info

cat /proc/cpuinfo
free
cat /proc/meminfo

#### ls command
-s is size of file in kilobytes
-h adds the human lettering for the file size

#### make new directory
mkdir

#### Access directories in schloss lab axiom and most modern mothur version
mnt/EXT/Schloss-data
/share/scratch/schloss/mothur/mothur

####Commands to install python locally

mkdir /home/masi/.local

cd Python-2.6.1
make clean
./configure --prefix=/home/masi/.local
make
make install

####Using the git command

#Create git directory and setting it up to be pushed to a Schloss Lab respository in git hub
git init
git add .
git commit -m "First commit"
git remote add origin https://github.com/SchlossLab/MSze_Project1_Control_Microbiome.git
git remote -v
git push origin master

#Change URL for the adding repository
git remote set-url origin https://github.com/SchlossLab/MSze_Project1_Control_Microbiome.git


#Add all changes to next commit to git repository
git add . 

#Observe what will be added to git repository
git status

#Add all changes to repository
git commit

#Exit text editor that is pulled up

:wq

#Alternative way
git commit -m '<message>'

#Submit job to axiom

qsub yourjob.pbs

#View Jobs on axiom

qstat
qstat your_job_number

#delete a job
qdel yourjobnumber


#Convert files from windows to linux on the command line

awk '{ sub("\r$", ""); print }' winfile.txt > unixfile.txt

and vice versa

awk 'sub("$", "\r")' unixfile.txt > winfile.txt

#Using the tr function instead of awk

tr -d '\15\32' < winfile.txt > unixfile.txt

##Download to server using wget and ftp
#This will download all files 
#So you can search and download by project
#Using NCBI database as a reference
# website ftp://ftp-trace.ncbi.nih.gov
# metadata might be found at http://www.ncbi.nlm.nih.gov/Traces/study/
#Example code below


wget -r -np - k ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP/SRP056/SRP056364/

#definitions:
	- r (recursive)
	- np (don't follow links to parent directories)
	- k (to make links in downloaded HTML or CSS point to local files)
	
#Other option definitions
	- nd (no directories)
	- e robots.off (ignore robot.txt files, dont download robots.txt files)
	-A png,jpg (accept only files with the extensions png or jpg)
	-m (mirror) (-r --timestamping --level inf --no-remove-listing)


##Convert SRA to specific file type

fastq-dump XXXXXXX.sra
sff-dump XXXXXXXX.sra


###Dowloading from MG-RAST and making a gzip file

curl http://api.metagenomics.an1.gov/1/download/mgmXXXXXX.3?file=XXX.X > mgmXXXXX.3/gz

##Ftp server download for HMP

ftp://public-ftp.hmpdacc.org/Illumina/PHASEII/stool/
ftp://public-ftp.hmpdacc.org/Illumina/stool/

##make shell file
chmod 755 XXXXXXX
chmod u+x XXXXX.sh

##Run file
./XXXXXXX

##List number of files of a specific type
ls -lR *.fna | wc -l

##List only specific files in a directory
ls -R | grep .pbs$

##Rename multiple files in bulk

rename 'xyz.file' 'xyz123.file' *file

## Find a specific sequence and get the line after it
#### The >> appends the selection to the bottom of the existing file.
#### The -w option means whole line must match
grep -w -A 1 'M00967_106_000000000-A9Y1K_1_2110_10786_12268' input.file >> test.fasta


## Downloading from dropbox
# Find a directory or file you want and select "share"
# From here select the "create link" option and copy it  
# EXTRA NOTE:
	# Need to make sure to change the end of the link from dl=0 to dl=1
	
		#download single file using a username and password (to be asked - best to use this interactively)
			wget --max-redirect=20 --user marcasze@gmail.com --ask-password 
			https://www.dropbox.com/s/rb35a072x3b079r/1.TCA.454Reads.fna?dl=1
			
		#download using a username and password a whole directory (zipped)
			wget -O weir.zip marcasze@gmail.com --ask-password 
			https://www.dropbox.com/sh/d35oug6b2k7blcx/AACSx4aPKIF1RCbB3r1koqwSa?dl=1
			
		#download a whole directory without using a username and passwork (zipped)
			wget -O weir.zip https://www.dropbox.com/sh/d35oug6b2k7blcx/AACSx4aPKIF1RCbB3r1koqwSa?dl=1









