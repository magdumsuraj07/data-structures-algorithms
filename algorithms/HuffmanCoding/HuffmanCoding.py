import heapq
import os


class BinaryTreeNode:
    '''
    Represents Binary Tree Node in Huffman Coding Algorithm
    '''
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq


class HuffmanCoding:
    '''
    Contains functionality to compress and decompress
    text files using Huffman Coding Algorithm.
    '''
    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}
    
    def __makeFrequencyDict(self, text):
        freqDict = {}
        for ch in text:
            freqDict[ch] = freqDict.get(ch, 0) + 1
        return freqDict

    def __buildHeap(self, freqDict):
        for ch, freq in freqDict.items():
            binaryTreeNode = BinaryTreeNode(ch, freq)
            heapq.heappush(self.__heap, binaryTreeNode)

    def __buildTree(self):
        while (len(self.__heap) > 1):
            binaryTreeNode1 = heapq.heappop(self.__heap)
            binaryTreeNode2 = heapq.heappop(self.__heap)
            newNode = BinaryTreeNode(None, binaryTreeNode1.freq + binaryTreeNode2.freq)
            newNode.left = binaryTreeNode1
            newNode.right = binaryTreeNode2
            heapq.heappush(self.__heap, newNode)

    def __buildCodesHelper(self, root, currBits):
        if (root is None):
            return
        if (root.value is not None):
            self.__codes[root.value] = currBits
            self.__reverseCodes[currBits] = root.value
            return
        self.__buildCodesHelper(root.left, currBits+"0")
        self.__buildCodesHelper(root.right, currBits+"1")

    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")

    def __getEncodedText(self, text):
        encodeText = ""
        for ch in text:
            encodeText += self.__codes[ch]
        return encodeText

    def __getPaddedEncodedText(self, encodedText):
        paddedAmount = 8 - (len(encodedText) % 8)
        encodedText += ('0' * paddedAmount)
        paddedInfo = "{0:08b}".format(paddedAmount)
        paddedEncodedText =  paddedInfo + encodedText
        return paddedEncodedText

    def __getBytesArray(self, paddedEncodedText):
        bytesArray = []
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i:i+8]
            bytesArray.append(int(byte, 2))
        return bytesArray


    def compress(self):
        '''
        Read text file and compress into binary file using Huffman Coding Algorithm
        '''

        # Get file from path
        fileName, fileExtension = os.path.splitext(self.path)
        outputPath = fileName + ".bin"

        # Read text from file
        with open(self.path, 'r+') as file, open(outputPath, 'wb') as output:
            text = file.read()
            text = text.rstrip()
            
            # Make frequency dictionary using the text
            freqDict = self.__makeFrequencyDict(text)

            # Construct the heap from the frequency dictionary
            self.__buildHeap(freqDict)

            # Construct binary tree from the heap
            self.__buildTree()

            # Construct the codes from binary tree
            self.__buildCodes()

            # Create encoded text using codes
            encodedText = self.__getEncodedText(text)

            # Padding encoded text
            paddedEncodedText = self.__getPaddedEncodedText(encodedText)

            # Convert encoded text to bytes
            bytesArray = self.__getBytesArray(paddedEncodedText)
            
            # Put this bytes into the file
            finalBytes = bytes(bytesArray)
            output.write(finalBytes)
        
        return outputPath

    def __removePadding(self, text):
        paddedInfo = text[:8]
        extraPadding = int(paddedInfo, 2)

        # Remove padding info and actual padding from text
        textAfterPaddingRemoved = text[8:(-1*extraPadding)]
        return textAfterPaddingRemoved

    def __decodeText(self, actualText):
        decodedText = ''
        currCode = ''
        for ch in actualText:
            currCode += ch
            if (currCode in self.__reverseCodes):
                decodedText += self.__reverseCodes[currCode]
                currCode = ''
        return decodedText


    def decompress(self, compressedFilePath):
        '''
        Read compressed binary file and decompress into text file using Huffman Coding Algorithm
        '''
        fileName, fileExtension = os.path.splitext(compressedFilePath)
        outputPath = fileName + "_decompressed" + ".txt"
        with open(compressedFilePath, 'rb') as file, open(outputPath, 'w') as output:
            bitString = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bitString += bits
                byte = file.read(1)

            actualText = self.__removePadding(bitString)

            decompressedText = self.__decodeText(actualText)
            output.write(decompressedText)