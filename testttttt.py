def input_and_write_data(filename):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Get input data from the user
        data_to_write = input("Enter data to overwrite the file: ")

        # Write the input data to the file
        file.write(data_to_write)

# Example usage
filename = "example.txt"
input_and_write_data(filename)
print(f"Data has been written to {filename}.")
