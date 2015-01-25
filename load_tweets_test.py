import unittest
import load_tweets


class LoadTweetsTest(unittest.TestCase):

    def test_make_list_from_dict(self):
        dictionary = {
            "thing1": "blah",
            "thing2": "haha",
            "dictionary": {"webster": True, "urbandict": False},
        }
        self.assertEqual(["blah", "haha"], load_tweets.make_value_list(dictionary))
        self.assertEqual([False, True], load_tweets.make_value_list(dictionary["dictionary"]))

if __name__ == "__main__":
    unittest.main()
