class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        soma_atual = 0
        indices = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                soma_atual = nums[i] + nums[j]
                if soma_atual == target:
                    indices.append([i, j])
                    break
                else:
                    soma_atual = 0
            if len(indices) > 0:
                break

        return(indices[0])