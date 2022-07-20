
Documentation

This script is made in python and is used to delete unused directories in the system that only occupy space with no reason.

It uses the os and shutil libraries.
Functions used in the code:
os.walk(path) → this function goes through the files and returns a tuple with:
1. Path of directory/file
2. Subdirectories
3. All the files in the directory
os.listdir(path) → this function lists all the files in a specific location.
Shutil.rmtree(path) → this functions assists in the deletion of the empty directories.

Pseudocode
import from os library
import from shutil
define a function directed to the path of the folder
function analyses the folders in the path
function sees if directories are empty inside the path
if directories are empty, function deletes them
else 
they’re not deleted.

code inspired and learned from https://www.codespeedy.com/how-to-delete-only-empty-folders-in-python/
