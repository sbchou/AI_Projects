import sys
from collections import defaultdict
from math import *
from copy import *

"""
sophie chou
sbc2125

learner.py

decision tree learning program.

given training data (csv file with attributes a_1...a_n, class) outputs python decision tree classifier

uses id3 algorithm 
"""

def parse(csv):
    "parse csv file, return list of lists per line"
    lines = []
    for line in open(csv):
        if line.strip():
            line = line.strip().split(",")
            lines.append(line)
    return lines

def sameness_check(examples):
    "return target if all targets the same, else return None"
    target = examples[0][-1]
    for example in examples:
        if example[-1] != target:
            return None
    return target


def plurality_value(examples):
    "return most common target value for given set of examples"
    counts = defaultdict(int)
    for example in examples:
        target = example[-1]
        counts[target] += 1
    return max(counts, key=counts.get)

def entropy(attribute, attribute_values, counts, examples, cond_attr=None, cond_val=None):
    "return entropy for an attribute given possible values and frequencies"
    entropy_value = 0.0
    
    if cond_attr == None and cond_val == None:
        values = attribute_values[attribute]
        for value in values:
            prob = counts[attribute, value]/sum(counts.values())
            if prob == 0.0:
                break
            entropy_value += -(prob)*log(prob, 2)

        return entropy_value

    else:
        subset = []
        for example in examples:
            if example[cond_attr] == cond_val:
                subset.append(example)
        new_values = get_values(subset)
        new_counts = get_counts(subset)
        prob = counts[cond_attr, cond_val]/sum(counts.values())
        cond_entropy = prob*entropy(attribute, new_values, new_counts, examples)
        return cond_entropy

def gain(attribute, target, attribute_values, counts, examples):
    "return the gaine or importance of an attribute. We use the definition of CONDITIONAL ENTROPY, where gain is H(Y) - H(Y|X), in this case H(Y|X) is the summation of the entropy of the target attribute among only those records where attribute X = v for each value v of X."
    goal_entropy = entropy(target, attribute_values, counts, examples)
    cond_entropy = 0.0
    for value in attribute_values[attribute]:
        cond_entropy += entropy(target, attribute_values, counts, examples, attribute, value)
    gain = goal_entropy - cond_entropy
    return gain

def best_attr(examples, attribute_values, counts):
    "return argmax of gain function"
    target = len(examples[0])-1
    attributes = attribute_values.keys()
    attributes.remove(target)
    best = None
    max_gain = -float("inf")    
    for attribute in attributes:
        current = gain(attribute, target, attribute_values, counts, examples)
        if current > max_gain:
            max_gain = current
            best = attribute
    return best

def get_counts(examples):
    "counts[attribute, value] returns its frequency. attributes include targets"
    counts = defaultdict(float)
    for example in examples:
        for attribute in range(len(example)):
            counts[attribute, example[attribute]] += 1

    return counts

def get_values(examples):
    "return list of posssible values for each attribute (including targets)"
    attribute_values = defaultdict(list)
    for example in examples:
        for attribute in range(len(example)):
            if example[attribute] not in attribute_values[attribute]:
                attribute_values[attribute].append(example[attribute])
    return attribute_values

def ID3(data, attribute_values, counts):
    data = deepcopy(data)
    if not data:
        return  
    vals = [record[-1] for record in data]
    default = plurality_value(data)

    if not data or (len(attribute_values.keys()) - 1) <= 0:
        return default

    elif vals.count(vals[0]) == len(vals):
        return vals[0]

    else:
        best = best_attr(data, attribute_values, counts)
        tree = {best:{}}

        for val in attribute_values[best]:
            new_attrs = deepcopy(attribute_values)
            new_attrs.pop(best)
            new_data = []
            for datum in data:
                if datum[best] == val:
                    new_data.append(datum)
            new_counts = get_counts(new_data)
            subtree = ID3(new_data, new_attrs, new_counts)
            tree[best][val] = subtree
    return tree

def create_script(tree):
    "Function that creates classification script given tree."
    string_tree = repr(tree)

    script = """
from tree_learner import parse
import sys

def classify(tree, case):
    while type(tree) == dict:
        index = tree.keys()[0]
        tree = tree[index][case[index]]
    return tree

def main(test_file):
    cases = parse(test_file)
    tree = """
    script += string_tree
    script += "\n"
    script += """
    for case in cases:
        print classify(tree, case)

if __name__ == '__main__': main(sys.argv[1])
    """

    tree_script = open("classifier.py", "w")
    tree_script.write(script)
    tree_script.close()

def main(training_file):
    examples = parse(training_file)
    attribute_values = get_values(examples)
    counts = get_counts(examples)
    tree = ID3(examples, attribute_values, counts)
    #print 'TREE'
    #print tree
    #import pdb
    #pdb.set_trace(
    create_script(tree)
  
if __name__ == '__main__': main(sys.argv[1])




