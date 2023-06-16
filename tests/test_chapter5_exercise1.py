from lib.chapter5_exercise1 import *

# test the format method returns a concatenated title 
# and contents with capitalised title title = 'Harry Potter' 
# contents = 'Some content' output = 'Harry Potter: some content'

def test_format_method() :
    new_entry = DiaryEntry('Harry Potter', 'some content')
    result = new_entry.format()
    assert result == 'Harry Potter: some content'

# test that the count_words method returns the correct number of words
# contents = 'some content' output = 2

def test_count_words() :
    new_entry = DiaryEntry('Harry Potter', 'some content')
    result = new_entry.count_words()
    assert result == 2
# test that the correct estimate is returned
# wpm = 5 words per min contents:'I really love Harry Potter' output = 1 min

def test_estimate_reading_time() :
    new_entry = DiaryEntry('Harry Potter', 'I really love Harry Potter')
    result = new_entry.reading_time(5)
    assert result == 1

# test that for the first call that it returns the correct number of words, 
# that for the second cal it returns the next chunk, and that it starts 
# again once finished 
# contents = 'I really love Harry Potter. This string should be broken up into chunks'
# wpm = 5 mins = 2 output first 10 words, then words 10-20 until finished then start again
def test_reading_chunk() :
    new_entry = DiaryEntry('Harry Potter', 'I really love Harry Potter. This string should be broken up into chunks')
    result = new_entry.reading_chunk(2,2)
    assert result == 'I really love Harry'

def test_reading_chunk_second_call() :
    new_entry = DiaryEntry('Harry Potter', 'I really love Harry Potter. This string should be broken up into chunks')
    new_entry.reading_chunk(2,2)
    result = new_entry.reading_chunk(2,3)
    assert result == 'Potter. This string should be broken'