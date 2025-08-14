class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # 배열을 정렬
        result = []
        
        for i in range(len(nums) - 2):
            # 중복된 i 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 중복된 left와 right 값 건너뛰기
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else: # current_sum > 0
                    right -= 1
                    
        return result