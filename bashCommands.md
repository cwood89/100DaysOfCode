# Bash Commands

## Move a file

To move a file the `mv` command is used. In your terminal type `mv [your file] [new destination]`.
If you're in the same directory as the file you want to move all you have to type in is the file name then use the relative path to your destination.

For example:
If you're in ths Documents folder and want to move a file named "image.jpg" to the Pictures folder you would type:
`~/Documents image.jpg ../Pictures`

You can also move all jpg files in a directory like this:
`~/Documents *.jpg ../Pictures`

## Wild Cards

The "*" is a wild card. It looks for partial files and grabs all of them. So in this case its grabbing all the files that end with ".jpg". The asterisk is also useful if you need to search for multiple files that contain a key word.
`run*` would return run, running, and runs.

There is also the "?" wild card. This looks for only a single unknown character. For example:
`ls file?.txt` will show file1.txt, file2.txt, file3.txt, ect.
If you need to search for two unknown characters you would just type `??`.s
