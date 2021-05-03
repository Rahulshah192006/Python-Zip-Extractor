from zipfile import ZipFile
file_path=str(input("Enter file location:"))
with ZipFile(file_path,'r') as zip:
    zip.printdir()
    print("Extracting Files")
    zip.extractall()
    print("Extraction Done")