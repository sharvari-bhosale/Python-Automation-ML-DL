import os                   # used for operating system and file/directory operations
import hashlib              # used for calculating file checksum

# This function calculates the MD5 checksum of the given file
def CalculateChecksum(FileName):

    fobj = open(FileName,"rb")                 # Open the file in binary read mode

    hobj = hashlib.md5()                       # Create an MD5 hash object

    Buffer = fobj.read(1024)                   # Read 1024 bytes from the file

    while(len(Buffer) > 0):                    # Continue until the end of the file
        hobj.update(Buffer)                    # Update the hash object with file data
        Buffer = fobj.read(1024)               # Read the next 1024 bytes from the file

    fobj.close()                               

    return hobj.hexdigest()                    # Return the MD5 checksum in hexadecimal format


# This function finds duplicate files from the given directory
def FindDuplicate(DirectoryName):

    Ret = False                                # Initialize the return value

    Ret = os.path.exists(DirectoryName)        # Check whether the given path exists

    if(Ret == False):                          # Check whether the path does not exist
        print("Path is invalid\n")              # Display an invalid path message
        return                                  # Return from the function

    Ret = os.path.isdir(DirectoryName)          # Check whether the path is a directory

    if(Ret == False):                           # Check whether the path is not a directory
        print("There is no such directory\n")   # Display a directory error message
        return                                  # Return from the function

    Duplicate = {}                              # Create an empty dictionary to store files by checksum

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):  # Traverse the directory and subdirectories

        for fName in FileName:                  # Iterate through every file in the directory
            fName = os.path.join(FolderName,fName)  # Create the complete path of the file

            CheckSum = CalculateChecksum(fName)     # Calculate the checksum of the file

            if(CheckSum in Duplicate):          # Check whether the checksum already exists in dictionary
                Duplicate[CheckSum].append(fName)   # Add the file to the existing checksum group

            else:
                Duplicate[CheckSum] = [fName]       # Create a new checksum group with the file

    return Duplicate                             # Return the dictionary containing files grouped by checksum


# This function deletes duplicate files from the given directory
def DeleteDuplicate(DirectoryName):

    MyDict = FindDuplicate(DirectoryName)       # Find duplicate files from the given directory

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))  # Select only groups having duplicate files

    Count = 0                                   # Initialize counter for duplicate files

    TotalDeleted = 0                            # Initialize total deleted file counter

    for Value in Result:                        # Iterate through each duplicate group

        for subValue in Value:                  # Iterate through each file in the duplicate group

            Count = Count + 1                   # Increment the file counter
            if Count > 1 :                      # Keep the first file and process the remaining files
                os.remove(subValue)             # Delete the duplicate file
                TotalDeleted = TotalDeleted + 1     # Increment the total deleted file count
        Count = 0                               # Reset the counter for the next duplicate group

    print("Total deleted files : ",TotalDeleted) # Display the total number of deleted files


# This is the main function that starts the duplicate file deletion process
def main():
    DeleteDuplicate("Test")                     

if __name__ == "__main__":                    
    main()                                      # Call the main function