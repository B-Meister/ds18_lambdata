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
    # user1 = SocialMediaUser('Jane')
    # self.assertEqual(user1.upvotes, 0)

    def setUp(self):
        """Common set up code run before all tests."""
        self.user1 = SocialMediaUser('Jane', 'Denmark')
        self.user2 = SocialMediaUser('Joe', 'Russia')

    def test_name(self):
        self.assertEqual(self.user1.name, 'Jane')
        self.assertEqual(self.user2.name, 'Joe')

    def test_location(self):
        self.assertEqual(self.user1.location, 'Denmark')
        self.assertEqual(self.user2.location, 'Russia')

    def test_default_upvotes(self):
        new_user = SocialMediaUser('Mary', 'Spain')
        self.assertEqual(new_user.upvotes, 0)

    def test_unpopular(self):
        """Test that a user with <= 100 upvotes is not popular."""
        new_user = SocialMediaUser('Bryce', 'US')
        self.assertFalse(new_user.is_popular())
        for _ in range(randint(1, 100)):
            new_user.receive_upvote()
        self.assertFalse(new_user.is_popular())

        # def test_unpopular(self):
        #     """Test that a user with <=100 upvotes is not popular."""
        #     user1 = SocialMediaUser('Joe')
        #     for _ in range(randint(1, 100)):
        #         user1.receive_upvote()

    def test_popular(self):
        """Test that a user with >100 upvotes is popular."""
        new_user = SocialMediaUser('Jordan', 'US')
        for _ in range(randint(101, 10000)):
            new_user.receive_upvote()
        self.assertTrue(new_user.is_popular())


if __name__ == '__main__':
    # This conditional is for code that will be run when we
    # execute our file from command line
    unittest.main()
