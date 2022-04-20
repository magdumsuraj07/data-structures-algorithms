class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(i, _target, subset):
            if i == len(candidates):
                if _target == 0:
                    res.append(subset[:])
                return

            # Include number
            if candidates[i] <= _target:
                subset.append(candidates[i])
                backtrack(i + 1, _target - candidates[i], subset)
                subset.pop()

            # Exclude number and its duplicates
            while (i + 1 < len(candidates)) and (candidates[i] == candidates[i + 1]):
                i += 1

            backtrack(i + 1, _target, subset)

        backtrack(0, target, [])
        return res
