###Reading a Sparse Matrix
## This function reads a sparse matrix from a text file and stores it in a dictionary format.
import os
import re

def read_sparse_matrix(file_path):
    sparse_matrix = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    parts = re.findall(r'-?\d+', line)
                    if len(parts) != 3:
                        print(f"Warning: Invalid line format: {line.strip()}")
                        continue
                    try:
                        row, col, value = map(int, parts)
                    except ValueError:
                        print(f"Warning: Invalid number format in line: {line.strip()}")
                        continue
                    
                    if row not in sparse_matrix:
                        sparse_matrix[row] = {}
                    sparse_matrix[row][col] = value
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading the file {file_path}: {e}")
    
    return sparse_matrix
##Subtracting Matrices
## This function subtracts the second sparse matrix from the first.
def subtract_matrices(matrix1, matrix2):
    result = {}
    for row in matrix1:
        result[row] = {}
        for col in matrix1[row]:
            result[row][col] = matrix1[row].get(col, 0) - matrix2.get(row, {}).get(col, 0)
    for row in matrix2:
        if row not in result:
            result[row] = {}
        for col in matrix2[row]:
            if col not in result[row]:
                result[row][col] = -matrix2[row][col]
    return result
## Multiplying Matrices
## This function multiplies two sparse matrices.
def multiply_matrices(matrix1, matrix2):
    result = {}
    for row1 in matrix1:
        for col2 in matrix2:
            for col1 in matrix1[row1]:
                if col1 in matrix2:
                    if row1 not in result:
                        result[row1] = {}
                    if col2 not in result[row1]:
                        result[row1][col2] = 0
                    result[row1][col2] += matrix1[row1][col1] * matrix2[col1].get(col2, 0)
    return result
## Main Function
## This function ties everything together, allowing the user to choose files and operations.
def main():
    try:
        files = os.listdir('.')
        matrix_files = [file for file in files if file.endswith('.txt')]

        print("Available matrix files:")
        for i, file in enumerate(matrix_files):
            print(f"{i+1}. {file}")

        # Choose the first matrix file
        choice1 = int(input("Choose the first matrix file (Enter the corresponding number): "))
        file1 = matrix_files[choice1 - 1]

        # Choose the second matrix file
        choice2 = int(input("Choose the second matrix file (Enter the corresponding number): "))
        file2 = matrix_files[choice2 - 1]

        # Read the matrices from the chosen files
        matrix1 = read_sparse_matrix(file1)
        matrix2 = read_sparse_matrix(file2)

        output_content = ""

        output_content += f"Matrix 1 ({file1}):\n"
        for row, cols in matrix1.items():
            for col, value in cols.items():
                output_content += f"{row} {col} {value}\n"

        output_content += f"\nMatrix 2 ({file2}):\n"
        for row, cols in matrix2.items():
            for col, value in cols.items():
                output_content += f"{row} {col} {value}\n"

        while True:
            print("\nChoose an operation:")
            print("1. Add matrix 1 and matrix 2")
            print("2. Subtract matrix 1 from matrix 2")
            print("3. Multiply matrix 1 by matrix 2")
            print("4. Exit")
            operation_choice = int(input("Enter your choice: "))

            if operation_choice == 1:
                result = add_matrices(matrix1, matrix2)
                print(result)
                operation_name = "Addition Result"
            elif operation_choice == 2:
                result = subtract_matrices(matrix1, matrix2)
                print(result)
                operation_name = "Subtraction Result"
            elif operation_choice == 3:
                result = multiply_matrices(matrix1, matrix2)
                print(result)
                operation_name = "Multiplication Result"
            elif operation_choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a number from 1 to 4.")
                continue

            output_content += f"\n{operation_name}:\n"
            for row, cols in result.items():
                for col, value in cols.items():
                    output_content += f"{row} {col} {value}\n"

        # Write the output to the file
        write_to_file("output.txt", output_content)
        print("Output saved to output.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
