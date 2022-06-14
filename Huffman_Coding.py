def split(word):
    return list(word)


class Node:  # create node class to enable node creation later on
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ""


code = dict()  # init dict to store code for each char


def calculateCodes(node, current=""):  # pass root node an empty string
    update = current + str(node.code)  # append str with .code value from each node

    if node.left:  # if child node exists
        calculateCodes(node.left, update)  # if True, call recursively to traverse through the tree

    if node.right:
        calculateCodes(node.right, update)  # # if True, call recursively to traverse through the tree

    if not node.left and not node.right:  # if leaf node, update dict for .char value of the node with the new updated code
        code[node.char] = update
        # print(code) Remove # to see tree being built

    return code


def decode(node, encoded_string):
    decoded = []
    el = list(encoded_string)
    print("encoded str split into chars *used for decoding*: ", el, "\n")
    root = node

    # print(encoded_string)

    while len(el) > 0:

        count = 0
        if int(el[0]) == 1 and node.char is None:  # if right path and not leaf
            el.pop(0)
            node = node.right
            # print(el)

        elif int(el[0]) == 0 and node.char is None:  # if left path and not leaf
            el.pop(0)
            node = node.left
            # print(el)

        elif node.char is not None:  # if leaf, append char to decoded
            while count == 0:  # counter to only append char once
                el.pop(0)
                # print(el)
                decoded.append(node.char)
                count += 1
                # reassigned node to original root, in order to start the  next iteration of the loop from the root node
                # node = root #problem is here, incorrect scope, as variable assignment is not returned  after the
                # loop completes.

    return decoded


def calculateFreqDict(text):  # split input String into char, count occurrence for each char
    char_list = split(text)
    setlist = set(char_list)
    freq_dict = {}
    for i in setlist:
        freq_dict[i] = char_list.count(i)

    #   order by ascending frequency
    ordered = {k: freq_dict[k] for k in sorted(freq_dict.keys(), key=freq_dict.__getitem__)}

    return ordered  # return dict with key (char) value (freq) in ascending order


def huffmanTree(text):
    char_freq = calculateFreqDict(text)  # calculate frequency
    chars = list(char_freq.keys())  # convert ordered chars to list (lowest first)
    freq = list(char_freq.values())  # convert ordered freq to list (lowest first)

    # print(chars)
    # print(freq)

    nodes = []  # init list of lists (tree)

    for i in range(len(chars)):  # loop through each character and create a node with values for char and frequency
        nodes.append(Node(freq[i], chars[i]))  # add to tree

    while len(nodes) > 1:  # loop until only 1 node remains (complete tree)
        rightChild = nodes[0]  # chars with lowest freq are paired together first
        leftChild = nodes[1]

        leftChild.code = 0  # assign binary value to use later for encoding
        rightChild.code = 1

        mergedNode = Node(leftChild.freq + rightChild.freq, None, leftChild, rightChild)  # merge nodes together

        nodes.remove(leftChild)  # remove nodes that have since been merged,
        nodes.remove(rightChild)
        nodes.append(mergedNode)  # new lowest nodes are  used in the next iteration, while the mergedNode is
        # placed at the end of the list
    print("codes for individual chars: ", calculateCodes(nodes[0]), "\n")
    print("Your String has been encoded: ", output(data, calculateCodes(nodes[0])), "\n")
    encoded = output(data, calculateCodes(nodes[0]))
    print("*INCORRECT, see decode function for details* Decoded String: ", decode(nodes[0], encoded), "\n")


def output(inputText, codes):  # convert full text to encoded counterpart
    encodedOutput = []  # init
    for i in inputText:
        encodedOutput.append(codes[i])  # append corresponding value for each char(key) in codes dict

    string = ''.join([str(item) for item in encodedOutput])
    return string


data = input("Enter a string to encode: ")
huffmanTree(data)

# print(encode(Huffman(data)))


# This algorithm works correctly to encode user input. It first takes the given string and splits the string up into
# individual characters -  (calculateFreqDict()) Then the characters are counted to find the frequency at which they
# appear in the string Each character is added into a dictionary as the dict_key, with their frequency used as the
# dict_value. The dictionary is put into ascending order, as to ensure that the algorithm uses the least occurring
# characters first. This function is then called from within HuffmanTree(), then the returned, ordered dictionary is
# split into two separate lists (char & freq) Each value is used to create a node for the tree, (subtree) The two
# lowest nodes are merged together and removed from the list, then the merged node is added to the list This repeats
# until only one node remains in the list, this is the full tree. Two more functions are used: To calculate the codes
# for each character, then to find the full encoded counterpart for the initial string. calculateCodes() recursively
# traverses the tree in pre-order, (starting from the root) to get the .code value for each node and appending it to
# a code value to be stored in a dict , then when reaching the leaf node, this code is added to the dict. output()
# finds the corresponding values for each char of the string that was initially input by the user and appends each
# code together, before returning the encoded value. The final function decode() is not functioning correctly as I
# ran out of time unfortunately, for details check the notes in the function I tried numerous methods to get this to
# work and believe I have pinpointed the issue though not yet found a solution.

# The complexity for this algorithm is O(log n)

