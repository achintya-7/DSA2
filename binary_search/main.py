from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0]) - 1
        height = len(matrix) - 1

        s = 0
        e = height
        m = 0        

        while s <= e:
            m = (s + e) // 2

            if matrix[m][width] == target:
                return True

            elif matrix[m][width] > target:
                if matrix[m][0] <= target: ## we found the row
                    break
                else:
                    e = m - 1

            else:
                s = m + 1

        s = 0
        e = width
        row = m

        while s <= e:
            m = (s + e) // 2 

            if matrix[row][m] == target:
                return True

            if matrix[row][m] > target:
                e = m - 1
            
            else:
                s = m + 1

        return False

if __name__ == '__main__':
    nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    obj = Solution()
    ans = obj.searchMatrix(nums, target)

    print(ans)
    
