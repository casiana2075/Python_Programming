#1.Create a Python script that does the following:
    # Takes a directory path and a file extension as command line arguments (use sys.argv).
    # Searches for all files with the given extension in the specified directory (use os module).
    # For each file found, read its contents and print them.
    # Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
import sys
import os    
try:
    if len(sys.argv) == 2 and os.path.splitext(sys.argv[1]) and os.path.splitext(sys.argv[1])[1].startswith(".") and \
        os.path.isdir(os.path.dirname(os.path.splitext(sys.argv[1])[0])):
            dir_path = os.path.dirname(os.path.splitext(sys.argv[1])[0])
            extension = os.path.splitext(sys.argv[1])[1]
    elif len(sys.argv) == 3:
        dir_path = sys.argv[1]
        extension = sys.argv[2]
        try:
            if not os.path.isdir(dir_path):
                raise Exception("Invalid directory path")
            if not extension.startswith("."):    
                raise Exception("Invalid file extension")
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        raise Exception("Please provide the directory path and file extension or a file path directly. To much or less arguments provided.")
    for (root,directories,files) in os.walk(dir_path):
        for file in files:
            if file.endswith(extension):
                print (file)
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        print(f.read())
                except IOError:
                    print(f"Error opening/reading file {file}")                    
except Exception as e:
    print (e)
    sys.exit(1) 
 #cmd : python Solution5.py C:\Users\casia\OneDrive\Documente\GitHub\Maxim_Casiana_B2-B4- .txt
 #cmd : python Solution5.py C:\Users\casia\OneDrive\Documente\GitHub\Maxim_Casiana_B2-B4-\file.txt
 
 
 
 #2.Write a script using the os module that renames all files in a specified directory to have a sequential
 #number prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory 
 #not existing or files that can't be renamed.
# import os
# import sys
# try:
#     dir_path = "C:\\Users\\casia\\OneDrive\\Documente\\GitHub\\Maxim_Casiana_B2-B4-\\Rename"
#     if not os.path.isdir(dir_path):
#         raise Exception("Invalid directory path")
#     i = 1
#     for file in os.listdir(dir_path):
#         if os.path.isfile(os.path.join(dir_path, file)):
#             if file.endswith(".txt"):
#                 os.rename(os.path.join(dir_path, file), os.path.join(dir_path, f"file{i}.txt"))
#                 i += 1 
#             else: 
#                 raise Exception(f"Invalid file extension for {file}")        
#     print ("Files renamed successfully") 
# except Exception as e:
#     print (e)
#     sys.exit(1)
    
    
#3.Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:
    # Use the sys module to read the directory path from the command line.
    # Utilize the os module to iterate through all the files in the given directory and its subdirectories.
    # Sum up the sizes of all files and display the total size in bytes.
    # Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.    
# import os
# import sys
# try:
#     if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
#         dir_path = sys.argv[1]
#     else:
#         raise Exception("Please provide a valid directory path")
#     total_size = 0
#     for (root,directories,files) in os.walk(dir_path):
#         for file in files:
#             try:
#                 total_size += os.path.getsize(os.path.join(root, file))
#             except OSError:
#                 print(f"Error accessing file {file}")
#     print(f"Total size of all files in directory {dir_path} is {total_size} bytes")
# except Exception as e:
#     print (e)
#     sys.exit(1)
#cmd : python Solution5.py C:\Users\casia\OneDrive\Documente\GitHub\Maxim_Casiana_B2-B4-\Rename


#4.Write a Python script that counts the number of files with each extension in a given directory. The script should:
    # Accept a directory path as a command line argument (using sys.argv).
    # Use the os module to list all files in the directory.
    # Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
    # Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.
# import os 
# import sys
# try:
#     if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
#         dir_path = sys.argv[1]
#     else:
#         raise Exception("Invalid input. Please provide a valid directory path")
#     extension_count = {}
#     for (root, directories, files) in os.walk(dir_path):
#         for file in files:
#             try:
#                 if os.path.isfile(file):
#                     extension = file.split(".")[-1]
#                     print (extension)
#                     if extension in extension_count:
#                         extension_count[extension] += 1
#                     else:
#                         extension_count[extension] = 1
#             except OSError:
#                 print(f"Error accessing file {file}")
#     if not extension_count:
#         raise Exception("No files found in the directory")
#     for key, value in extension_count.items():
#         print(f"Number of files with extension {key}: {value}")
# except Exception as e:
#     print(e)
#     sys.exit(1)