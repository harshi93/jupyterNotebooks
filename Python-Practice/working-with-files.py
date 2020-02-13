#TODO Working with files


"""
A file can be opened in reading, writing, appending and reading/writing mode
positional arguments 'r' = reading, 'w' = writing, 'a' = appending, 'r+' = reading and writing
"""

#TODO open files in sub-optimal way

"""

It is important that we explicitly close the file if use this way to open the files
otherwise we will eventually run out of file descriptors and this can also
lead to memory leaks as well
  
"""


f = open('.gitignore')

print(f.mode)

f.close()


#TODO open and read file using context managers

"""
The upside of using context manager for opening files is file gets closed automatically 
as soon as we exit the block or there is an exception

1) f.readline() - reads one line at a time
2) f.readlines() - reads all of the file at a time
3  The below approach is the most efficient approach as it doesn't takes in all of the data into memory
    
  for line in f:
       print(line, end='')

"""

with open('.gitignore', 'r') as f:
    f_contents = f.read()
    print(f_contents);


# TODO open and read content of a file, few character at a time

    with open('.gitignore', 'r') as f:
        size_to_read = 100

        f_contents = f.read(size_to_read)

        while len(f_contents) > 0:
            print(f_contents, end='');
            f_contents = f.read(size_to_read)



# TODO print your current position in a file


    with open('.gitignore', 'r') as f:
        size_to_read = 10

        f_contents = f.read(size_to_read)

        print(f.tell())



# TODO read x characters from a file and print same x characters


    with open('.gitignore','r') as f:
        size_to_read = 5

        f.seek(5) # Do more reading about effective use of seek

        f_contents = f.read(size_to_read)
        print(f_contents)


# TODO read from a file and write to another file


    with open('.gitignore','r') as rf:
        with open('.gitignore_copy', 'w') as wf:
            for line in rf:
                wf.write(line)



# TODO read a small sized chunk from a image file and write to another image file


    with open('comic.png', 'rb') as rf:
        with open('comic_copy.png', 'wb') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)