class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. 배열의 뒤에서부터 첫 번째로 감소하는 숫자 찾기
        # 이 숫자의 인덱스를 i라고 합니다.
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # 2. 그런 숫자가 있다면 (i >= 0)
        if i >= 0:
            # i의 오른쪽에서 nums[i]보다 큰 첫 번째 숫자 찾기
            # 이 숫자의 인덱스를 j라고 합니다.
            j = n-1
            while j > 0 and nums[j] <= nums[i]:
                j -=1
            # nums[i]와 nums[j]의 위치 바꾸기
            nums[i], nums[j] = nums[j], nums[i]

        # 3. i+1부터 배열 끝까지 뒤집기
        # 이 부분은 이미 내림차순으로 정렬되어 있으므로 뒤집는 것이
        # 가장 빠른 오름차순 정렬 방법입니다.
        
        # 만약 i가 -1이라면, 배열 전체가 내림차순이므로
        # 전체를 뒤집어 가장 작은 순열(오름차순)을 만듭니다
        left = i+1
        right = n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1

        