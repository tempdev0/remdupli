# Python script to remove duplicate lines or URLs from a file

def remove_duplicates(input_file, output_file):
    """
    Remove duplicate lines or URLs from a file
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    unique_lines = list(set(lines))  # Remove duplicates using set
    unique_lines = [line.strip() for line in unique_lines]  # Remove trailing newlines
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(unique_lines))  # Write unique lines to output file

# Get input file from user
input_file = input("Enter the input file path: ")

# Get output file from user
output_file = input("Enter the output file path: ")

# Call the function to remove duplicates
remove_duplicates(input_file, output_file)

print("Duplicates removed successfully!")
