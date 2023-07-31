# This file contain a overview list of python modules, in alphabetical order

# sys.argv - enables you to retrieve command-line arguments. Is an array or data structure. First position = 0 and is the program name
            # second position = 1 contains the first argument.
# Code example
import sys
print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg


#venv module - creates a vritual environment where your python program is run with all dependencies it needs without affecting other installed versions of python etc. 
                # Code: "python -m venv Env" - is run as a terminal command
                # ! never put your program files in the env directory. Rather put program files in a directory called src
                
                # to ACTIVATE a virtual environment:
                    # Console: c:\...\env\Scripts\activate
                    # Bash: source env/bin/activate    eg. go to bin folder and write "source activate" in bash temrinal. 
                    # you know when it i activated by (env) path/to/project
                # to step out of the virtual environment -> Console: deactivate