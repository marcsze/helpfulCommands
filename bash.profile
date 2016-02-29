# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin
export PATH
alias python='/usr/bin/python2.7'
cd /mnt/EXT/Schloss-data/msze
module load qpeek

#Readable code format for custom fonts

set_prompt () {
	Last_Command=$? # Must come first
	Blue='\[\e[01;34m\]'
	White='\[\e[01;37m\]'
	Red='\[\e[01;31m\]'
	Green='\[\e[01;32m\]'
	Reset='\[\e[00m\]'
	FancyX='\342\234\227'
	Checkmark='\342\234\223'
	Cyan='\[\e[01;36m\]'

	#### Add a bright white exit status for the last command
	PS1="$White\$? "
	##### If it was successful, print a green check mark. Otherwise, print
	##### a red X
	if [[ $Last_Command == 0 ]]; then
		PS1+="$Green$Checkmark "
	else
		PS1+="$Red$FancyX "
	fi
	##### If root, just print the host in red. Otherwise, print the current user
	##### and host in green.
	if [[ $EUID == 0 ]]; then
		PS1+="$Red\\h "
	else
		PS1+="$Green\\u@\\h "
	fi
	##### Print the working directory and prompt marker in cyan, and reset
	##### the text color to the default.
	PS1+="$Cyan\\W \\\$$Reset "
}
PROMPT_COMMAND='set_prompt'

**Do not run the below commnads**
This is the raw command for mods implemented above
PS1="\[\033[01;37m\]\$? \$(if [[ \$? == 0 ]]; then echo \"\[\033[01;32m\]\342\234\223\"; else echo \"\[\033[\033[01;31m\]\342\234\227\"; fi) $(if [[ ${EUID} == 0 ]]; then echo '\[\033[01;31m\]\h'; else echo '\[\033[01;32m\]u@\h'; fi)\[\033[01;34m\] \W \$\[\033[00m\] "


PS1='\[\e[0;32m\]\u\[\e[m\] \[\e[1;34m\]\W\[\e[m\] \[\e[1;32m\]\$\[\e[m\] \[\e[1;37m\]'

Helpful guide to the code 
 The string above contains color-set escape sequences
	(start coloring: \[\e[color\], end coloring: \[\e[m\])
	and info paceholders:
		\u - Username. Original prompt also has \h (host name)
		\w - Current absolute path. Use \W for relative path
		\$ - The prompt character (eg # for root and $ for regular)
		\[and\] - These tags should be placed around color codes so bash knows how to properly place the cursor.
 The last color-set sequence, \[\e[1;37m\], is not closed, so the remaining text (everything typed into the terminal, 
 program output and son on) will be in that (bright white) color.  It may be desirable to change this color, or to delete the last escape sequence in order to leave the actual output in unaltered color.
