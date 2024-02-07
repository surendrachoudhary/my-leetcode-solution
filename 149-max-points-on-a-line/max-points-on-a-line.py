class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                count = 2  # Initial count for the current pair of points

                # Calculate the differences in x and y coordinates between two points
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Iterate through all points to check if they lie on the same line
                for k in range(n):
                    if k != i and k != j:
                        dx_ = points[k][0] - points[i][0]
                        dy_ = points[k][1] - points[i][1]

                        # If the cross product is zero, the points are collinear
                        if dx_ * dy == dy_ * dx:
                            count += 1  # Increment count if the point lies on the same line

                result = max(result, count)  # Update the maximum count

        return result
