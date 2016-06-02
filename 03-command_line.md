# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`touch` Creates an empty file or updates the timestamp if the file already exists.
`cat` Streams a file or files to standard output.
`find` Searches for files in a given directory hierarchy(recursively).
`grep` Searches within a file or files for lines matching a pattern. 
`pushd` Pushes current directory onto a stack while changing directories.
`popd` Takes you to the top directory in the stack created with `pushd`.
`echo` Displays a line of text. 
`mkdir` Creates a new directory.
`chmod` Changes permissions (read, write, execute) on a file.
`w` Tells you who is logged in and what they're doing.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls` Lists the contents of a directory. `ls -a` Includes hidden dot files. `ls -l` Lists contents in long form, including permissions, owner, group, size, and timestamp.
`ls -lh` Renders the size in human-readable format. `ls -lah` Adds hidden dotfiles to the longform, human-readable list of contents.
`ls -t` Sorts the contents by modification time, newest first. `ls -Glp` Lists directory contents in longform minus the group, including a trailing indicator slash for directories.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -r` Lists contents in reverse order.
`ls -R` Displays contents recursively.
`ls -1` Displays each entry on it's own line.
`ls -x` Displays files across the whole screen.
`ls -d` Displays directories only.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` reads from standard input and executes a command, essentially a way to combine commands on the command line. 
A common example is piping the output of the `find` command into `xargs`. 
`find . -name "*.txt" -print | xargs /bin/rm`
This finds ".txt" files in or below the current directory and deletes them. 

 

