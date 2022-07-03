class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        for i in range(numRows - 1):
            new = [1]
            for j in range(0, i):
                new.append(triangle[i][j] + triangle[i][j+1])
            new.append(1)
            triangle.append(new)
        return triangle
        