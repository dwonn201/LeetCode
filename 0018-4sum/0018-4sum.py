class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []

        # fix first number
        for i in range(n-3): 
            # skip if duplicated
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # fix second number
            for j in range(i+1, n-2):
                # skip if duplicated
                if j > i +1 and nums[j] == nums[j-1]:
                    continue
                
                left, right = j + 1, n-1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1
                    
                        # skip if next number is same as before
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        # skip if previous number is same as after
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif current_sum < target:
                        left += 1
                    else: 
                        right -=1 
        return output
            


            




        