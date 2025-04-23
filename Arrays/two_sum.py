class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        soma_atual = 0
        indices = []
        i = 0
        j = 1

        while i < j and j < len(nums):
            soma_atual = nums[i] + nums[j]
            if soma_atual == target:
                indices.append([i, j])
                break
            else:
                i += 1
                j += 1

        return(indices[0])