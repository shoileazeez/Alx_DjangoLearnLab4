import shutil

# Define the source path and the destination path
source = '\LibraryProject\bookshelf\README.md'
destination = '\LibraryProject'

# Move the file
shutil.move(source, destination)

print(f"File moved from {source} to {destination}")
