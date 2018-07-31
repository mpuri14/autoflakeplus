# autoflakeplus

Autoflake is a tool created by https://github.com/myint which removes unused imports and unused variables from Python code. It makes use of pyflakes to do this.

This script can be used to perform autoflake operation inside a folder. The script recursively looks for python files inside the folder and any subdirectories inside it. 

It makes a backup of each python file it finds before performing the autoflake. 

After the operation, it compares the contents of the original file with the backup file and delete the backup file if no changes were made to the original file.


