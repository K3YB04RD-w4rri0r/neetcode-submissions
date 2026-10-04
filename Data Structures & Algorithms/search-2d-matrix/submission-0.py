class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1 
        lc, rc = 0, len(matrix[0]) - 1

        # first need to constrain the row
        while lr < rr:
            mid = lr + (rr - lr + 1) // 2   # upper mid
            if matrix[mid][0] <= target:
                lr = mid
            else:
                rr = mid - 1
                
        # second constraining the olumn
        while lc < rc:
            midpointc = lc + (rc - lc) // 2
            if matrix[lr][midpointc] < target:
                lc = midpointc + 1 
            else:
                rc = midpointc
        print(rc)
        return True if matrix[lr][lc] == target else False

        

        