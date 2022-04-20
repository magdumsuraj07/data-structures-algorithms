class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(i, _target, subset):
            if i == len(candidates):
                if _target == 0:
                    res.append(subset[:])
                return

            # Include current number
            if candidates[i] <= _target:
                subset.append(candidates[i])
                backtrack(i, _target - candidates[i], subset)
                subset.pop()

            # Exclude current number
            backtrack(i + 1, _target, subset)

        backtrack(0, target, [])
        return res
