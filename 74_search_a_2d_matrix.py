'''
Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the
    previous row.

'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Save the number of rows and columns of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search checking first and last element of the middle row
        first_row, last_row = 0, ROWS - 1
        
        while first_row <= last_row:
            middle_row = (first_row + last_row) // 2
            if target < matrix[middle_row][0]:
                last_row = middle_row - 1
            elif target > matrix[middle_row][-1]:
                first_row = middle_row +1
            else:
                break

        # Check if row is valid
        if first_row > last_row:
            return False

        # Binary search on the row itself to find the target
        first_column, last_column = 0, COLS - 1

        while first_column <= last_column:
            middle_column = (first_column + last_column) // 2
            if matrix[middle_row][middle_column] < target:
                first_column = middle_column + 1
            elif matrix[middle_row][middle_column] > target:
                last_column = middle_column - 1
            else:
                return True
        
        return False


def main():
    solution = Solution()

    test = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
        ]
    print(solution.searchMatrix(test, 3))

    test = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
        ]
    print(solution.searchMatrix(test, 23))
    

if __name__ == '__main__':
    main()