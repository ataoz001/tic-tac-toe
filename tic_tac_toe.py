def check(matrix):
    matrix = matrix

    def vertical(matrix):
        for i in range(3):
            if matrix[i] != ". ":
                if matrix[i] == matrix[i + 3] and matrix[i + 3] == matrix[i + 6]:
                    return 1
        return 0

    def horizontal(matrix):
        i = 0
        while i < 8:
            if matrix[i] != ". ":
                if matrix[i] == matrix[i + 1] and matrix[i + 1] == matrix[i + 2]:
                    return 1
            i = i + 3
        return 0

    def diagonal(matrix):
        for i in range(2):
            if matrix[0] != ". " and matrix[2] != ". ":
                if matrix[0] == matrix[4] and matrix[1] == matrix[8]:
                    return 1
                elif matrix[2] == matrix[4] and matrix[2] == matrix[6]:
                    return 1
        return 0

    return diagonal(matrix), vertical(matrix), horizontal(matrix)


if __name__ == "__main__":
    print(check(["X ", "X ", ". ", ". ", "X ", "O ", "O ", "O ", "O "]))
    if any(check(["X ", "X ", ". ", ". ", "X ", "O ", "O ", "O ", "O "])):
        print("you win")
