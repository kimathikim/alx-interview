#!/usr/bin/env python3
import sys


def print_usage_and_exit(message):
    print(message)
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, results):
    if col >= len(board):
        result = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == 1:
                    result.append([r, c])
        results.append(result)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, results)
            board[i][col] = 0  # Backtrack

    return res


def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    results = []
    solve_nqueens(board, 0, results)
    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Invalid number of arguments")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)
