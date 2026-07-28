# ========================================# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4: Matrix Operations
# =============================================================================

def read_matrix(rows, cols, matrix_name=""):
    """Helper function to read a matrix of size rows x cols from the user."""
    label = f" for {matrix_name}" if matrix_name else ""
    print(f"\nEntering elements{label} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row_str = input(f"  Enter row {i + 1}: ")
        row = [int(val) for val in row_str.strip().split()]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Helper function to print a matrix in a neat grid format."""
    for row in matrix:
        for val in row:
            print(f"{val:4d}", end="")
        print()


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """
    Computes the transpose of a matrix (rows become columns, columns become rows).
    Input matrix size: M x N -> Output matrix size: N x M
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty result matrix of size N x M
    transposed = []

    # Loop through each column of the original matrix to create new rows
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """
    Computes the element-wise sum of two matrices of the same size (M x N).
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            sum_val = matrix_a[i][j] + matrix_b[i][j]
            row.append(sum_val)
        result.append(row)

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Computes the product of matrix A (M x N) and matrix B (N x P).
    Result is of size M x P.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Initialize M x P result matrix filled with 0s
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            row.append(0)
        result.append(row)

    # Compute dot products using 3 nested loops
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================
def main():
    print("==========================================")
    print("        PART A: MATRIX TRANSPOSE          ")
    print("==========================================")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix = read_matrix(m, n)
    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)

    print("\n" + "=" * 42)
    print("        PART B: MATRIX ADDITION           ")
    print("==========================================")
    m = int(input("Enter number of rows for both matrices: "))
    n = int(input("Enter number of columns for both matrices: "))

    matrix_a = read_matrix(m, n, "Matrix A")
    matrix_b = read_matrix(m, n, "Matrix B")

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)

    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nSum (A + B):")
    display_matrix(sum_matrix)

    print("\n" + "=" * 42)
    print("     PART C: MATRIX MULTIPLICATION        ")
    print("==========================================")
    m = int(input("Enter number of rows for Matrix A (M): "))
    n = int(input("Enter number of columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter number of columns for Matrix B (P): "))

    matrix_a = read_matrix(m, n, "Matrix A")
    matrix_b = read_matrix(n, p, "Matrix B")

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)

    product_matrix = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct (A x B):")
    display_matrix(product_matrix)


if __name__ == "__main__":
    main()