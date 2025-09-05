# file_handling_example.py

# 1. Writing to a file (creates file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("We are learning file handling in Python.\n")

print("✅ File created and data written.")

# 2. Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("\n📖 Content of the file after writing:")
    print(content)

# 3. Appending to a file
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

print("✅ Data appended to the file.")

# 4. Reading again to see appended data
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\n📖 Content of the file after appending:")
    print(updated_content)
