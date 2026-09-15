class Solution:
    # Define the class required by LeetCode.

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # nums  = input array
        # target = required sum
        # We return the indices of the two numbers.

        mydict = {}
        # Create an empty dictionary.
        # We will store:
        # number -> its index
        #
        # Example:
        # {2: 0}
        # means number 2 was found at index 0.

        for i in range(len(nums)):
            # Go through the array one element at a time.
            # i is the current index.

            needed = target - nums[i]
            # Calculate what number is needed to make the target.
            #
            # Example:
            # target = 9
            # current number = 2
            #
            # needed = 9 - 2
            #        = 7
            #
            # So we need to find 7.

            if needed in mydict:
                # Check whether the needed number
                # has already appeared in the array.

                return [mydict[needed], i]
                # mydict[needed] gives the previous index.
                # i gives the current index.
                #
                # Example:
                # 2 was previously stored at index 0
                # current 7 is at index 1
                #
                # return [0, 1]

            mydict[nums[i]] = i
            # The needed number was not found.
            # So store the current number and its index.
            #
            # Example:
            # nums[i] = 2
            # i = 0
            #
            # mydict becomes:
            # {2: 0}
result = Solution().twoSum([2, 7, 11, 15], 9)
print(result)



            #---------------------------------------------------------------------------------------------------------------------------------
class Solution:
    # Define the class required by LeetCode.

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # numbers = sorted input array
        # target = required sum
        # We return 1-based indices.

        left = 0
        # left starts at the first element of the array.

        right = len(numbers) - 1
        # right starts at the last element of the array.

        while left < right:
            # Continue until the two pointers meet.
            # We need two different elements.

            total = numbers[left] + numbers[right]
            # Calculate the sum of the elements
            # currently pointed to by left and right.

            if total == target:
                # We found the required pair.

                return [left + 1, right + 1]
                # The problem requires 1-based indices.
                #
                # Python uses:
                # 0, 1, 2, 3
                #
                # Problem wants:
                # 1, 2, 3, 4
                #
                # So add 1 to both indices.

            elif total < target:
                # The current sum is too small.
                #
                # Because the array is sorted,
                # moving left to the right gives us
                # a larger number.

                left += 1
                # Move left one position forward.

            else:
                # The current sum is too large.
                #
                # Because the array is sorted,
                # moving right to the left gives us
                # a smaller number.

                right -= 1
                # Move right one position backward.


result = Solution().twoSum([2, 7, 11, 15], 9)
print(result)