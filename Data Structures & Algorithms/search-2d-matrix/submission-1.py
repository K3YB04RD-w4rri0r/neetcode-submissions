class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1 
        lc, rc = 0, len(matrix[0]) - 1

        while lr < rr:
            mid = lr + (rr - lr) // 2
            if matrix[mid][0] < target:
                lr = mid + 1
            else:
                rr = mid

        if matrix[lr][0] > target:   # overshot: target belongs in the previous row
            if lr == 0:
                return False         # smaller than everything
            lr -= 1

        # second constraining the olumn
        while lc < rc:
            midpointc = lc + (rc - lc) // 2
            if matrix[lr][midpointc] < target:
                lc = midpointc + 1 
            else:
                rc = midpointc
        print(rc)
        return True if matrix[lr][lc] == target else False

        

        