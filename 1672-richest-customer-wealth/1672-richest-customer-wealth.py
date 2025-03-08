class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_list = []
        for account in accounts:
            num = 0
            for i in range(len(account)):
                num += account[i]
            max_list.append(num)
        return max(max_list)
        