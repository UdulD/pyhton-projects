def load_matrices(filename="matrix_data.txt"):
    all_matrices = []
    with open(filename, "r") as file:
        content = [line.strip() for line in file if line.strip()]
    pos = 0
    count = int(content[pos])
    pos += 1
    for i in range(count):
        size = int(content[pos])
        pos += 1
        mat = []
        for j in range(size):
            values = content[pos].split(",")
            mat.append([int(v) for v in values])
            pos += 1
        all_matrices.append(mat)
    return all_matrices


def calc_determinant(mat):
    size = len(mat)
    if size == 1:
        return mat[0][0]
    if size == 2:
        return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])
    total = 0
    for j in range(size):
        sub = get_minor(mat, 0, j)
        total += ((-1) ** j) * mat[0][j] * calc_determinant(sub)
    return total


def get_minor(mat, i, j):
    result = []
    for r in range(len(mat)):
        if r == i:
            continue
        new_row = []
        for c in range(len(mat[r])):
            if c == j:
                continue
            new_row.append(mat[r][c])
        result.append(new_row)
    return result


def get_transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(mat[r][c])
        result.append(new_row)
    return result


def find_inverse(mat):
    size = len(mat)
    det = calc_determinant(mat)
    cof_mat = []
    for r in range(size):
        cof_row = []
        for c in range(size):
            sub = get_minor(mat, r, c)
            cof_val = ((-1) ** (r + c)) * calc_determinant(sub)
            cof_row.append(cof_val)
        cof_mat.append(cof_row)
    adjoint = get_transpose(cof_mat)
    inv = []
    for r in range(size):
        inv_row = []
        for c in range(size):
            inv_row.append(adjoint[r][c] / det)
        inv.append(inv_row)
    return inv


def show_results(inv_list):
    for i in range(len(inv_list)):
        print(f"Inverse of Matrix {i + 1}:")
        for row in inv_list[i]:
            print("".join(f"{val + 0.0:7.2f}" for val in row))


def main():
    matrices = load_matrices("matrix_data.txt")
    results = []
    for mat in matrices:
        results.append(find_inverse(mat))
    show_results(results)


main()
