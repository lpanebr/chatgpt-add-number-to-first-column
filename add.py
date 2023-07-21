import sys

def process_line(line, increment):
    if line.startswith('#'):
        return line  # Preserve the commented lines as they are

    columns = line.split()
    if len(columns) != 3:
        return None  # Ignore lines with incorrect format

    try:
        num1 = int(columns[0])
        num1 += increment
        num2 = float(columns[1])
        num3 = float(columns[2])
        return f"{num1}\t{num2}\t{num3}\n"
    except ValueError:
        return None  # Ignore lines with non-numeric values

def main(filename, increment):
    try:
        increment = int(increment)
        with open(filename, 'r') as file:
            output = ""
            for line in file:
                processed_line = process_line(line.strip(), increment)
                if processed_line is not None:
                    output += processed_line

        # Output the processed data to the console or a new file
        print(output)
        # If you want to save it to a file, you can do the following:
        # with open("output.txt", "w") as out_file:
        #     out_file.write(output)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: The increment value should be an integer.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <increment>")
    else:
        filename = sys.argv[1]
        increment = sys.argv[2]
        main(filename, increment)

