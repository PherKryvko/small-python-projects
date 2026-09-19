"""

6: What is the time complexity of looping through every element once?

7: What kind of variable is this:

count = 0

when it changes while looping?
"""




"""
1: Given:

nums = [3, 5, 2, 8, 1]

write code to count how many values are greater than 4.
"""
class QuestionOne():

    @staticmethod
    def total_greater(numbers):
        total_greater = 0

        for num in numbers:
            if num > 4:
                total_greater += 1

        return total_greater

"""
2: Given:

word = "mississippi"

count how many times "s" appears.
"""
class QuestionTwo():

    @staticmethod
    def s_count(word):
        tally = word.count("s")

        return tally

"""
3: Given:

nums = [7, 2, 10, 4]

find the largest value manually using iteration.
"""

class QuestionThree():

    @staticmethod
    def largest_num(num_array):
        current_largest = num_array[0]

        for nums in num_array:
            if current_largest < nums:
                current_largest = nums

        return current_largest

"""4: Given:

nums = [1, 3, 5, 8]

return True if 8 exists, otherwise False."""

class QuestionFour():

    @staticmethod
    def eight_exist_check(nums):
        if 8 in nums:
            return True
        return False

"""
5: Which would you use when you need both position and value?

for item in items
or
enumerate(items)

"""


if __name__ == "__main__":
    nums = [3, 5, 2, 8, 1]

    result = QuestionOne.total_greater(nums) #Since its a static method it doesn't need an instance of itself

    print(result)

    result = QuestionTwo.s_count("mississippi")

    print(result)

    nums_2 = [7, 2, 10, 4]
    result = QuestionThree.largest_num(nums_2)

    print(result)

    nums_3 = [1, 3, 5, 8]
    result = QuestionFour.eight_exist_check(nums_3)

    print(result)

