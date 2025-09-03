# Step 1: Create input.txt with sample content
with open("input.txt", "w") as infile:
    infile.write("My name is Martha.\n")
    infile.write("I love coding.\n")
    infile.write("This is a python code.\n")
    infile.write("Python is a versatile language.\n")
    infile.write("Code with me today!\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 3: Count the number of words
word_count = len(content.split())

# Step 4: Convert all text to uppercase
uppercase_content = content.upper()

# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("PROCESSED TEXT:\n")
    outfile.write(uppercase_content + "\n")
    outfile.write(f"WORD COUNT: {word_count}\n")

# Step 6: Print success message
print("✅ Success! 'output.txt' has been created with the processed content.")
