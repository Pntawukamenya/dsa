import re

class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        self.matrix = {}
        if matrix_file_path:
            self.read_matrix(matrix_file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols

    def read_matrix(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        self.num_rows = int(lines[0].strip().split('=')[1])
        self.num_cols = int(lines[1].strip().split('=')[1])
        
        pattern = re.compile(r"\((\d+),\s*(\d+),\s*(-?\d+)\)")
        for line in lines[2:]:
            line = line.strip()
            if not line:
                continue
            match = pattern.match(line)
            if not match:
                raise ValueError("Input file has wrong format")
            row, col, value = map(int, match.groups())
            self.matrix[(row, col)] = value

    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for key in self.matrix:
            result.set_element(key[0], key[1], self.get_element(*key))
        for key in other.matrix:
            result.set_element(key[0], key[1], result.get_element(*key) + other.get_element(*key))
        return result

    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for key in self.matrix:
            result.set_element(key[0], key[1], self.get_element(*key))
        for key in other.matrix:
            result.set_element(key[0], key[1], result.get_element(*key) - other.get_element(*key))
        return result

    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (i, k), v in self.matrix.items():
            for j in range(other.num_cols):
                result.set_element(i, j, result.get_element(i, j) + v * other.get_element(k, j))
        return result

def main():
    base_path = '/dsa/sparse_matrix/sample_inputs/'
    filenames = [
        "easy_sample_01_1.txt", "easy_sample_01_2.txt",
        "easy_sample_02_1.txt", "easy_sample_02_2.txt",
        "easy_sample_03_1.txt", "easy_sample_03_2.txt",
        "easy_sample_04_1.txt", "easy_sample_04_2.txt"
    ]

    for i in range(0, len(filenames), 2):
        matrix1_path = base_path + filenames[i]
        matrix2_path = base_path + filenames[i+1]

        matrix1 = SparseMatrix(matrix1_path)
        matrix2 = SparseMatrix(matrix2_path)

        addition_result = matrix1 + matrix2
        subtraction_result = matrix1 - matrix2
        multiplication_result = matrix1 * matrix2

        print(f"Results for {filenames[i]} and {filenames[i+1]}:")
        print("Addition Result:", addition_result.matrix)
        print("Subtraction Result:", subtraction_result.matrix)
        print("Multiplication Result:", multiplication_result.matrix)
        print()

if __name__ == "__main__":
    main()
