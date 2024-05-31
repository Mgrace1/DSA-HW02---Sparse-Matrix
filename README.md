# Sparse Matrix Operations

This project provides a Python script for performing various operations on sparse matrices, including addition, subtraction, and multiplication. The matrices are read from text files and the results are saved to an output file.

## Features

- Read sparse matrices from text files.
- Add, subtract, and multiply sparse matrices.
- Save the results of operations to an output file.

## Requirements

- Python 3.x

## Usage

1. **Prepare the Matrix Files:**

   Ensure you have the matrix files in the same directory as the script. Each matrix file should contain lines with three integers separated by spaces. Each line represents a non-zero element in the matrix in the format:
   
row_index col_index value

Example of a matrix file (`matrix1.txt`):


2. **Run the Script:**

Execute the script using Python. You will be prompted to select the matrix files and the operation to perform.

```bash
python matrix.py

3. **follow the prompts**
The script will list the available matrix files in the directory. Enter the number corresponding to the files you want to use.

Example prompt:
Available matrix files:
1. matrix1.txt
2. matrix2.txt

Choose the first matrix file (Enter the corresponding number): 1
Choose the second matrix file (Enter the corresponding number): 2
4. **Choose the Operation**:

After selecting the matrix files, choose the operation you want to perform:
Choose an operation:
1. Add matrix 1 and matrix 2
2. Subtract matrix 1 from matrix 2
3. Multiply matrix 1 by matrix 2
4. Exit
Enter the number corresponding to the desired operation.

5. **View the Results**:

The result of the operation will be printed to the console and saved to an output file named output.txt.

Example output file (output.txt):
Matrix 1 (matrix1.txt):
0 0 5
0 1 8
1 0 3

Matrix 2 (matrix2.txt):
0 0 2
1 1 6

Addition Result:
0 0 7
0 1 8
1 0 3
1 1 6


Run the script:

    python matrix.py
