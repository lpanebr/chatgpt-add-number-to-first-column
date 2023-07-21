import sys

def process_line(line, increment, column_widths):
    if line.startswith('#'):
        return line  # Preserve the commented lines as they are

    columns = line.split()
    if len(columns) != 3:
        return None  # Ignore lines with incorrect format

    try:
        num1 = int(columns[0]) + increment
        num2 = float(columns[1])
        num3 = float(columns[2])
        return "{:<{}} {:<{}} {:<{}}\n".format(num1, column_widths[0], num2, column_widths[1], num3, column_widths[2])
    except ValueError:
        return None  # Ignore lines with non-numeric values

def main(filename, increment):
    try:
        increment = int(increment)
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Find the maximum width of each column
            column_widths = [max(len(column.strip()) for column in line.split()) for line in lines if not line.startswith('#')]
            
            output = ""
            is_comment = False
            for line in lines:
                if line.startswith('#'):
                    output += line
                    is_comment = True
                elif is_comment:
                    output += line
                    is_comment = False
                else:
                    processed_line = process_line(line.strip(), increment, column_widths)
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

