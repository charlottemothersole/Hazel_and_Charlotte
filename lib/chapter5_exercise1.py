class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.words = []

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        new_title = self.title.title()
        return new_title + ": " + self.contents
    

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return self.count_words()/wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        readable_words = wpm * minutes
        chunk = self.contents.split()[0:readable_words]
        self.words = len(chunk)
        print(self.words)
        second_chunk = self.contents.split()[self.words:readable_words]
        
        return ' '.join(second_chunk)