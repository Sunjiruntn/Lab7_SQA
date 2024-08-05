import unittest

class CountClump:
    """
    This class provides a method to count the number of "clumps" in a list of integers.
    A clump is a run of 2 or more of the same adjacent numbers.
    """

    @staticmethod
    def count_clumps(nums):
        """
        Counts the number of "clumps" in a list of integers.
        A clump is a run of 2 or more of the same adjacent numbers.

        Args:
          nums: A list of integers.

        Returns:
          The number of clumps in the list.
        """
        if nums is None or len(nums) == 0:
            return 0

        count = 0
        prev = nums[0]
        in_clump = False

        for i in range(1, len(nums)):
            if nums[i] == prev and not in_clump:
                in_clump = True
                count += 1
            elif nums[i] != prev:
                prev = nums[i]
                in_clump = False

        return count

class TestCountClump(unittest.TestCase):

    def test_T1(self):
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_T2(self):
        self.assertEqual(CountClump.count_clumps(None), 0)

    def test_T3(self):
        self.assertEqual(CountClump.count_clumps([1]), 0)

    def test_T4(self):
        self.assertEqual(CountClump.count_clumps([2, 3, 4, 5, 6]), 0)

    def test_T5(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 3, 4]), 1)

    def test_T6(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 2, 3, 3]), 3)

    def test_T7(self):
        self.assertEqual(CountClump.count_clumps([2, 2, 2, 2, 2]), 1)

    def test_T8(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 2, 3, 4, 4, 4, 1]), 3)

if __name__ == '__main__':
    unittest.main()
