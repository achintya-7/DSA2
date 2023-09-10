from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        if len(heights) == 1:
            return heights[0]

        ans = self.better(heights)

        return ans

    def better(self, heights: List[int]) -> int:
        maxArea = 0

        n = len(heights)
        left_smaller = n * [0]
        stack = []

        for i, a in enumerate(heights):
            while stack and a <= heights[stack[-1]]:
                stack.pop()

            if stack:
                left_smaller[i] = stack[-1] + 1
            else:
                left_smaller[i] = 0

            stack.append(i)

        print(left_smaller)

        right_smaller = n * [0]
        stack = []

        for i, a in reversed(list(enumerate(heights))):
            while stack and a <= heights[stack[-1]]:
                stack.pop()

            if stack:
                right_smaller[i] = stack[-1] - 1
            else:
                right_smaller[i] = n - 1

            stack.append(i)

        print(right_smaller)

        for i in range(n):
            height = heights[i]
            left = left_smaller[i]
            right = right_smaller[i]
            area = height * (right - left + 1)

            maxArea = max(maxArea, area)

        return maxArea
        
    def brute(self, heights: List[int]) -> int:
        maxArea = 0
        
        for i, a in enumerate(heights):
            l = 1

            t = i
            # finding left border
            while t > 0 and a < heights[t-1]:
                t -= 1
                l += 1

            t = i
            # finding right border
            while t < len(heights) - 1 and a < heights[t+1]:
                t += 1
                l += 1

            maxArea = max(maxArea, l * a)

        return maxArea 


if __name__ == "__main__":
    obj = Solution()

    heights = [2,1,5,6,2,3,1]
    ans = obj.largestRectangleArea(heights)
    print(ans)