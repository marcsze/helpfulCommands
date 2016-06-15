###General Linux Commands

**Login command**

ssh -l msze compute01 -X

**Upload file**

scp file.txt msze@compute01:/home/msze/data/

**Upload file to second server** 

scp -r Hogg_Run505 msze@compute01:/home/msze/data/

**Download file**

scp msze@compute01:/home/msze/data/file.txt

**Adding a new PATH to commands**
**(Has to be in parent directory to set it up)**

PATH=$PATH:/home/msze/data/bowtie2/bowtie2-2.1.0/bowtie2-build/:home/msze/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:; export PATH

**Link (Soft) command/program with bin folder**
**allows PATH function to search bin for command and not have to retype PATH every login**

ln -s /home/msze/data/bowtie2-build /home/msze/bin/bowtie2-build

**List number of files of a specific type**

ls -lR *.fna | wc -l

**List only specific files in a directory**

ls -R | grep .pbs$

**list of file and directory sizes to a text file**

du -hs * | sort -h > diskusage.txt

**View Bash profile (view bash proifle file to view customizations)

nano .bash_profile


**Server/computer info**

*cat /proc/cpuinfo
*free
*cat /proc/meminfo


**Short commands**

*pwd -> print working directory
*cd -> change directory
*du -h -> directory size
*rm -r -> remove a directory
*rm -> remove a file
*cat -> combine two files (cat file1 file2 > new.file)
*ls -> list (combined with -s and -h to get file size as well)
*mkdir -> make a new directory
*chmod u+x XXXXX.sh -> make a shell file (use ./XXXXXXX to run)
./XXXXXXX


**Axiom commands**

*qsub -> submit a job
*qstat -> get current jobs (combine with -u and username to be more specific)
*qdel -> delete a job (use job number)

**Unzip commands**

*unzip -j filename.zip
*tar zxvf fileNameHere.tgz
*gzip -d file.gz
*gunzip file.gz
*bzip2 -d filename.bz2

**Download commands**

*Download to server using wget and ftp

wget -r -np - k ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP/SRP056/SRP056364/

definitions:
	- r (recursive)
	- np (don't follow links to parent directories)
	- k (to make links in downloaded HTML or CSS point to local files)
	
Other option definitions
	- nd (no directories)
	- e robots.off (ignore robot.txt files, dont download robots.txt files)
	-A png,jpg (accept only files with the extensions png or jpg)
	-m (mirror) (-r --timestamping --level inf --no-remove-listing)


This will download all files 
So you can search and download by project
Using NCBI database as a reference
website ftp://ftp-trace.ncbi.nih.gov
metadata might be found at http://www.ncbi.nlm.nih.gov/Traces/study/

*Dowloading from MG-RAST and making a gzip file

curl http://api.metagenomics.an1.gov/1/download/mgmXXXXXX.3?file=XXX.X > mgmXXXXX.3/gz

*Downloading from Dropbox*  
1. Find a directory or file you want and select "share"
2.  From here select the "create link" option and copy it  
3. EXTRA NOTE:
	* Need to make sure to change the end of the link from dl=0 to dl=1
	
* Download single file using a username and password (to be asked - best to use this interactively)
	* `wget --max-redirect=20 --user marcasze@gmail.com --ask-password https://www.dropbox.com/s/rb35a072x3b079r/1.TCA.454Reads.fna?dl=1`
  	
* Download using a username and password a whole directory (zipped)
	* `wget -O weir.zip marcasze@gmail.com --ask-password https://www.dropbox.com/sh/d35oug6b2k7blcx/AACSx4aPKIF1RCbB3r1koqwSa?dl=1`
  			
* Download a whole directory without using a username and passwork (zipped)
	* `wget -O weir.zip https://www.dropbox.com/sh/d35oug6b2k7blcx/AACSx4aPKIF1RCbB3r1koqwSa?dl=1`


**Convert SRA to specific file type**

*fastq-dump XXXXXXX.sra
*sff-dump XXXXXXXX.sra











