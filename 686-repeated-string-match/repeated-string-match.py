class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum number of times to repeat a
        min_repeats = -(-len(b) // len(a))  # Equivalent to ceil(len(b) / len(a))

        # Concatenate a repeated min_repeats times and check if b is a substring
        repeated_a = a * min_repeats
        if b in repeated_a:
            return min_repeats

        # If b is not a substring of a repeated min_repeats times, check if it is a substring after repeating one more time
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1

        # If b is still not a substring after repeating one more time, return -1
        return -1
