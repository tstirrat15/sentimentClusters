import dataset
import argparse
import string


def parse_line(line, label):
    """Takes a space-separated line from the community file, separates
    into id_str tokens, and returns a list of dictionaries for updating
    the database"""
    tokens = line.split(" ")
    return [{"id_str": token, "community": label} for token in tokens]

if __name__ == '__main__':
    parser = argparse.ArgumentParser("""Takes the ouput of a GANXiS document as
        input, and updates the given tweet database with a categorical
        variable based on which group the tweets were in""")
    parser.add_argument("input", help="Input file - output of GANXiS program")
    parser.add_argument("database", help="Database to update: should be the original source of the data")
    args = parser.parse_args()

    with open(args.input, "r") as community_file:
        with dataset.connect("sqlite:///" + args.database) as db:
            # Give a None if there's no key. This'll be useful for
            # orphaned nodes in the original network.
            categories = {}

            letter_generator = (char for char in string.ascii_lowercase)

            for line in community_file:
                community = parse_line(line, next(letter_generator))
                for member in community:
                    db['tweets'].update(member, ["id_str"])
