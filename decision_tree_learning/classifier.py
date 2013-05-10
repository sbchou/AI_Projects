
from tree_learner import parse
import sys

def classify(tree, case):
    while type(tree) == dict:
        index = tree.keys()[0]
        tree = tree[index][case[index]]
    return tree

def main(test_file):
    cases = parse(test_file)
    tree = {0: {'None': 'No', 'Full': {7: {'10-30': 'Yes', '30-60': 'Yes', '0-10': 'No', '>60': {2: {'Nope': 'Yes', 'Yeah': {4: {'$$': 'Maybe', '$': 'No', '$$$': {5: {'Nope': 'No', 'Yeah': 'Maybe'}}}}}}}}, 'Some': {4: {'$$': 'Yes', '$': {2: {'Nope': 'Yes', 'Yeah': 'Maybe'}}, '$$$': 'Yes'}}}}

    for case in cases:
        print classify(tree, case)

if __name__ == '__main__': main(sys.argv[1])
    