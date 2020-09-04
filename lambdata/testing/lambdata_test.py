""" The Testing Script for DS 18 Lambdata."""

import unittest
from random import randint

from example_module import increment, COLORS
from oop_examples import SocialMediaUser


class ExampleUnitTests(unittest.TestCase):
    """ Making sure our examples behave as expected"""

    def test_increment(self):
        """Testing the increment function to add one to a number"""
        x1 = 9
        y1 = increment(x1)
        x2 = -157
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 10)
        self.assertEqual(y2, -157)

    def test_increment_random(self):
        """Test incrementing a random integer"""
        x1 = randint(1, 1000000)
        y1 = increment(x1)
        self.assertEqual(y1, x1 + 1)

    def test_colors(self):
        """Tests to make sure there are certain colors in the given list"""
        self.assertIn('White', COLORS)
        self.assertNotIn('Rainbow', COLORS)
        self.assertEqual(len(COLORS), 7)


class SocialMediaUserTests(unittest.TestCase):
    """Tests the instantiation and use of SocialMediaUser"""
    user1 = SocialMediaUser('Jane')
    self.assertEqual(user1.upvotes, 0)

    def test_unpopular(self):
        """Test that a user with <=100 upvotes is not popular."""
        user1 = SocialMediaUser('Joe')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()


if __name__ == '__main__':
    # This conditional is for code that will be run when we
    # execute our file from command line
    unittest.main()
