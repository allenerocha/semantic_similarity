class synonyms:
    def __init__(self, urls: list) -> None:
        for url in urls:
            if type(url) != str:
                raise TypeError("URLs must be strings")

    def parse_corpus(self, urls: str):
        pass
        # This method should:
        # 1. Open each URL in turn.
        # 2. Read the URL a sentence at a time. To read a sentence one sentence at a time, you can set the delimiter of
            # your scanner with useDelimiter ( "[\\.\\?\\!]|\\Z" ) .
        # 3. Split the sentence into words, stripping out punctuation and making the words lowercase.
        """
        Notes:
            An easy way to strip out punctuation is to use replaceAll ( \\W+, "" ) .
            The String class has a split() method. If you split around "\\s+" you will be splitting the
            sentence around whitespace characters.
            The LMS has an example of how to read URL’s.
        """

    def calculate_cosine_similarity(self, word1: str, word2: str) -> float:

        pass
        """
        A public method that computes the Cosine Similatity of two words. If you look at the formula above,
        you see that there are three sums computed: one vector dot product, and two vector magnitudes.
        The correct way to tackle this is to write two private methods to make these calculations.
        There is one special case: word1 or word2 might not appear anywhere in the corpus. If this is true,
        your method should return a similarity value of -1.0 .
        """



"""
   Output
    Enter a word:
    vexed
    Enter the choices
    synonym annoyed book spellbound
        synonym -1.0
        annoyed 0.6924426938376693
        book 0.082729574126462
        spellbound 0.6391785522199395
    annoyed
    
    Enter a word:
    provincial
    Enter the choices
    rural cosmopolitan forested horse
        rural 0.8741068346646507
        cosmopolitan 0.42806939662558796
        forested -1.0
        horse 0.8668406391340332
        rural
"""

