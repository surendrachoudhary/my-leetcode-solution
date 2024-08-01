class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        for index, color in enumerate(colors):
            if (colors[(index-1)%n] ) != color and color != (colors[(index+1)%n]):
                count += 1
        return count 