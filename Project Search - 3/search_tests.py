from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                        ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                        ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.






def test_music_unit_tests():

    assert search('music') == MUSIC
    assert search('Music') == MUSIC

    # Advanced search option 1, function #4
    expected = {'List of Canadian musicians': {'author': 'Bearcat', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Brandon', 'timestamp': 1172208041, 'length': 5569}, 'Noise (music)': {'author': 'Epbr123', 'timestamp': 1194207604, 'length': 15641}, '1922 in music': {'author': 'Jafeluv', 'timestamp': 1242717698, 'length': 11576}, '1986 in music': {'author': 'Michael', 'timestamp': 1048918054, 'length': 6632}, 'Kevin Cadogan': {'author': 'Renesis', 'timestamp': 1144136316, 'length': 3917}, '2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'Rock music': {'author': 'Sabrebd', 'timestamp': 1258069053, 'length': 119498}, 'Lights (musician)': {'author': 'Espo3699', 'timestamp': 1213914297, 'length': 5898}, 'Tim Arnold (musician)': {'author': 'Sohohobo', 'timestamp': 1181480380, 'length': 4551}, 'Old-time music': {'author': 'Badagnani', 'timestamp': 1124771619, 'length': 12755}, 'Arabic music': {'author': 'Badagnani', 'timestamp': 1209417864, 'length': 25114}, 'Joe Becker (musician)': {'author': 'Gary King', 'timestamp': 1203234507, 'length': 5842}, 'Richard Wright (musician)': {'author': 'Bdubiscool', 'timestamp': 1189536295, 'length': 16185}, 'Voice classification in non-classical music': {'author': 'Iridescent', 'timestamp': 1198092852, 'length': 11280}, '1936 in music': {'author': 'JohnRogers', 'timestamp': 1243745950, 'length': 23417}, '1962 in country music': {'author': 'Briguy52748', 'timestamp': 1249862464, 'length': 7954}, 'List of dystopian music, TV programs, and games': {'author': 'Notinasnaid', 'timestamp': 1165317338, 'length': 13458}, 'Steve Perry (musician)': {'author': 'Woohookitty', 'timestamp': 1254812045, 'length': 22204}, 'David Gray (musician)': {'author': 'RattleandHum', 'timestamp': 1159841492, 'length': 7203}, 'Alex Turner (musician)': {'author': 'CambridgeBayWeather', 'timestamp': 1187010135, 'length': 9718}, 'List of gospel musicians': {'author': 'Absolon', 'timestamp': 1197658845, 'length': 3805}, 'Indian classical music': {'author': 'Davydog', 'timestamp': 1222543238, 'length': 9503}, '1996 in music': {'author': 'Kharker', 'timestamp': 1148585201, 'length': 21688}, 'Traditional Thai musical instruments': {'author': 'Badagnani', 'timestamp': 1191830919, 'length': 6775}, '2006 in music': {'author': 'Suduser85', 'timestamp': 1171547747, 'length': 105280}, 'Tony Kaye (musician)': {'author': 'Bondegezou', 'timestamp': 1141489894, 'length': 8419}, 'Texture (music)': {'author': 'J Lorraine', 'timestamp': 1161070178, 'length': 3626}, '2007 in music': {'author': 'Squilly', 'timestamp': 1169248845, 'length': 45652}, '2008 in music': {'author': 'Ba11innnn', 'timestamp': 1217641857, 'length': 107605}}
    assert article_info(deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Kevin Cadogan', 'Tim Arnold (musician)', 'List of gospel musicians', 'Texture (music)']
    assert article_length(5000, deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'List of Canadian musicians': 1181623340, 'French pop music': 1172208041, 'Noise (music)': 1194207604, '1922 in music': 1242717698, '1986 in music': 1048918054, 'Kevin Cadogan': 1144136316, '2009 in music': 1235133583, 'Rock music': 1258069053, 'Lights (musician)': 1213914297, 'Tim Arnold (musician)': 1181480380, 'Old-time music': 1124771619, 'Arabic music': 1209417864, 'Joe Becker (musician)': 1203234507, 'Richard Wright (musician)': 1189536295, 'Voice classification in non-classical music': 1198092852, '1936 in music': 1243745950, '1962 in country music': 1249862464, 'List of dystopian music, TV programs, and games': 1165317338, 'Steve Perry (musician)': 1254812045, 'David Gray (musician)': 1159841492, 'Alex Turner (musician)': 1187010135, 'List of gospel musicians': 1197658845, 'Indian classical music': 1222543238, '1996 in music': 1148585201, 'Traditional Thai musical instruments': 1191830919, '2006 in music': 1171547747, 'Tony Kaye (musician)': 1141489894, 'Texture (music)': 1161070178, '2007 in music': 1169248845, '2008 in music': 1217641857}
    assert title_timestamp(deepcopy(MUSIC), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Davydog', deepcopy(MUSIC), TITLE_TO_INFO) == True
    assert favorite_author('Aman', deepcopy(MUSIC), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(MUSIC)) == expected
    
    
    
def test_soccer_unit_tests():

    # Basic search, function #3
    assert search('soccer') == SOCCER
    assert search('socceR') == SOCCER

    # Advanced search option 1, function #4
    expected = {'Spain national beach soccer team': {'author': 'Pegship', 'timestamp': 1233458894, 'length': 1526}, 'Will Johnson (soccer)': {'author': 'Mayumashu', 'timestamp': 1218489712, 'length': 3562}, 'Steven Cohen (soccer)': {'author': 'Scouselad10', 'timestamp': 1237669593, 'length': 2117}}
    assert article_info(deepcopy(SOCCER), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Spain national beach soccer team']
    assert article_length(2000, deepcopy(SOCCER), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Spain national beach soccer team': 1233458894, 'Will Johnson (soccer)': 1218489712, 'Steven Cohen (soccer)': 1237669593}
    assert title_timestamp(deepcopy(SOCCER), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Pegship', deepcopy(SOCCER), TITLE_TO_INFO) == True
    assert favorite_author('Jack Sparrow', deepcopy(SOCCER), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog'] 
    assert multiple_keywords('dog', deepcopy(SOCCER)) == expected
    
    

def test_place_unit_tests():

    # Basic search, function #3
    assert search('place') == PLACE
    assert search('pLACE') == PLACE

    # Advanced search option 1, function #4
    expected = {'2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'List of dystopian music, TV programs, and games': {'author': 'Notinasnaid', 'timestamp': 1165317338, 'length': 13458}, '2006 in music': {'author': 'Suduser85', 'timestamp': 1171547747, 'length': 105280}, '2007 in music': {'author': 'Squilly', 'timestamp': 1169248845, 'length': 45652}, '2008 in music': {'author': 'Ba11innnn', 'timestamp': 1217641857, 'length': 107605}} 
    assert article_info(deepcopy(PLACE), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['List of dystopian music, TV programs, and games']
    assert article_length(20000, deepcopy(PLACE), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'2009 in music': 1235133583, 'List of dystopian music, TV programs, and games': 1165317338, '2006 in music': 1171547747, '2007 in music': 1169248845, '2008 in music': 1217641857}
    assert title_timestamp(deepcopy(PLACE), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Squilly', deepcopy(PLACE), TITLE_TO_INFO) == True
    assert favorite_author('Bruce', deepcopy(PLACE), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music', 'C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)'] 
    assert multiple_keywords('programming', deepcopy(PLACE)) == expected   
    
    
    
    
@patch('builtins.input')
def test_integration_dog_1(input_mock):
    keyword = 'dog'
    advanced_option = 1

    output = get_print(input_mock, [keyword, advanced_option])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}\n"  
    


@patch('builtins.input')
def test_integration_music_2(input_mock):
    keyword = 'music'
    advanced_option = 2
    advanced_response = 10000

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['French pop music', '1986 in music', 'Kevin Cadogan', 'Lights (musician)', 'Tim Arnold (musician)', 'Joe Becker (musician)', '1962 in country music', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', 'Traditional Thai musical instruments', 'Tony Kaye (musician)', 'Texture (music)']\n"
    
    
    
@patch('builtins.input')
def test_integration_soccer_3(input_mock):
    keyword = 'soccer'
    advanced_option = 3

    output = get_print(input_mock, [keyword, advanced_option])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'Spain national beach soccer team': 1233458894, 'Will Johnson (soccer)': 1218489712, 'Steven Cohen (soccer)': 1237669593}\n"
    


@patch('builtins.input')
def test_integration_school_4(input_mock):
    keyword = 'school'
    advanced_option = 4
    advanced_response = 'NerdyScienceDude'
    
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + advanced_response + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)'] \nYour favorite author is not in the returned articles!\n"   
    
        
@patch('builtins.input')    
def test_integration_dog_5(input_mock):
    keyword = 'dog'
    advanced_option = 5
    advanced_response = 'music'

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + advanced_response + "\n\nHere are your articles: ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n" 
    
 
    
@patch('builtins.input')
def test_integration_programming_6(input_mock):
    keyword = 'programming'
    advanced_option = 6
    output = get_print(input_mock, [keyword, advanced_option])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)'] \n"        
    



def test_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''

    fake_metadata_1 = [['Fisk University', 'random', 12345, 103, ['tenessee', 'nashville', 'hbcu', 'jubilee', 'american', 'african']],
                        ['TSU', 'random_2', 9871, 802, ['tenessee', 'nashville', 'hbcu', 'jubilee', 'american', 'african']]]
    expected = {'Fisk University': {'author': 'random', 'timestamp': 12345, 'length': 103}, 
                'TSU': {'author': 'random_2', 'timestamp': 9871, 'length': 802}}
                
    assert title_to_info(deepcopy(fake_metadata_1)) == expected
    
    
    fake_metadata_2 = []
    expected = {}
    assert title_to_info(deepcopy(fake_metadata_2)) == expected
    
    
    fake_metadata_3 = [['The Alchemist', 'paulo', 123456, 103, ['sun', 'moon', 'desert', 'sky', 'omen', 'destiny']]]
    expected = {'The Alchemist': {'author': 'paulo', 'timestamp': 123456, 'length': 103}}
                
    assert title_to_info(deepcopy(fake_metadata_3)) == expected
    
    
    
    
def test_keyword_to_titles():
    ''' Tests for keyword_to_titles(), function #2. '''

    fake_metadata_1 = [['Fisk University', 'random', 12345, 103, ['tenessee', 'nashville', 'hbcu', 'jubilee', 'american', 'african']],
                        ['TSU', 'random_2', 9871, 802, ['tenessee', 'nashville', 'hbcu', 'nonjubilee', 'american', 'african']]]
    expected = {'tenessee': ['Fisk University', 'TSU'], 'nashville': ['Fisk University', 'TSU'], 'hbcu': ['Fisk University', 'TSU'], 'jubilee': ['Fisk University'], 'american': ['Fisk University', 'TSU'], 'african': ['Fisk University', 'TSU'], 'nonjubilee': ['TSU']}

    assert keyword_to_titles(deepcopy(fake_metadata_1)) == expected 
    
    
    fake_metadata_2 = []
    expected = {}
    assert keyword_to_titles(deepcopy(fake_metadata_2)) == expected
    
    
    fake_metadata_3 = [['The Alchemist', 'paulo', 123456, 103, ['sun', 'moon', 'desert', 'sky', 'omen', 'destiny']]]
    expected = {'sun': ['The Alchemist'], 'moon': ['The Alchemist'], 'desert': ['The Alchemist'], 'sky': ['The Alchemist'], 'omen': ['The Alchemist'], 'destiny': ['The Alchemist']}
   
    assert keyword_to_titles(deepcopy(fake_metadata_3)) == expected


# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    test_music_unit_tests()
    test_soccer_unit_tests()
    test_place_unit_tests()
    test_integration_dog_1()
    test_integration_music_2()
    test_integration_soccer_3()
    test_integration_school_4()
    test_integration_dog_5()
    test_integration_programming_6()
    test_title_to_info_tests()
    test_keyword_to_titles()
    
    
