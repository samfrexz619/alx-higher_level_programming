#!/usr/bin/python3
write_file = __import__('2-append_write').append_write

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
