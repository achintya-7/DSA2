from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterArray = self.nextGreaterElementArray(nums1, nums2)
        print("building answer")
        ans = self.answerBuilder(nums1, nums2, nextGreaterArray)
        return ans
    
    def nextGreaterElementArray(self, nums1, nums2):
        n = len(nums2)
        stack = []
        ans = [-1] * n

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(nums2[i])
            
        return ans

    def answerBuilder(self, nums1, nums2, array):
        ans = []
        
        for num in nums1:
            ans.append(array[nums2.index(num)])

        return ans

    def findNext(self, i, nums2):
        found = False
        for a, b in enumerate(nums2):
            if b != i and found == False:
                continue
            else:
                found = True

            if b > i:
                return b
        
        return -1



            

if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    obj = Solution()
    ans = obj.nextGreaterElement(nums1, nums2)

    print(ans)
