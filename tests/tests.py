from src.aoc.aoc_client import AdventOfCodeBase
from src.common.display import Display


SOURCE = 'say hello, to my little friend! Codename_47-2002'
SOURCE_MULTILINES = 'say hello, to my little friend!\nCodename_47-2002'
YEAR, DAY = '2022', '3'
LONG_YEAR, REQUEST_DAY = YEAR, DAY
TITLE = 'Codename 47'
DISPLAY = 10
URL = 'https://adventofcode.com/{year}/day/{day}'
LEVEL_A = 'a'
LEVEL_B = 'b'
PART_1 = '8053'
PART_2 = '2425'


class Test(Display, AdventOfCodeBase):
    @classmethod
    def test_solver_functions(cls):
        # print(cls.read_raw('.setup.cfg'))
        # print(cls.write_file('delete_this'))

        assert cls.make_list(str, SOURCE) == ['s', 'a', 'y', ' ', 'h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'o', ' ', 'm', 'y', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 'f', 'r', 'i', 'e', 'n', 'd', '!', ' ', 'C', 'o', 'd', 'e', 'n', 'a', 'm', 'e', '_', '4', '7', '-', '2', '0', '0', '2']
        assert cls.make_tuple(str, SOURCE) == ('s', 'a', 'y', ' ', 'h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'o', ' ', 'm', 'y', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 'f', 'r', 'i', 'e', 'n', 'd', '!', ' ', 'C', 'o', 'd', 'e', 'n', 'a', 'm', 'e', '_', '4', '7', '-', '2', '0', '0', '2')

        assert cls.str_split(SOURCE) == ['say', 'hello,', 'to', 'my', 'little', 'friend!', 'Codename_47-2002']
        assert cls.str_strip(SOURCE) == 'say hello, to my little friend! Codename_47-2002'
        assert cls.paragraph(SOURCE) == ['say hello, to my little friend! Codename_47-2002']

        assert cls.each_first_item(YEAR) == ['2', '0', '2', '2']
        assert cls.each_item(YEAR) == ['2', '0', '2', '2']
        assert cls.check_len_string(SOURCE) is True
        assert cls.strings_per_line(SOURCE_MULTILINES) == ['say hello, to my little friend!', 'Codename_47-2002']

        assert cls.truncate(obj='say hello', width=99) == 'say hello'
        assert cls.truncate(obj='say hello', width=7) == 'say ...'

        assert cls.integers(SOURCE) == (47, -2002)
        assert cls.positive_integers(SOURCE) == (47, 2002)
        assert cls.find_digit(SOURCE) == (4, 7, 2, 0, 0, 2)
        assert cls.find_strings(SOURCE) == ('say', 'hello', 'to', 'my', 'little', 'friend', 'Codename')
        return
    
    #@classmethod
    # def test_display(cls):
    #     assert cls.helper_base(
    #         source=SOURCE,
    #         year=YEAR,
    #         title=TITLE,
    #         display_type='paragraph',
    #         parser_method='integers',
    #         display=DISPLAY
    #     ) == ('say', 'hello')
    #     assert cls.helper_base(
    #         source=SOURCE_MULTILINES,
    #         year=YEAR,
    #         title=TITLE,
    #         display_type='paragraph',
    #         parser_method='find_digit',
    #         display=DISPLAY
    #     ) == ((1, 2, 3), (7,))
    # 
    #     return

    @classmethod
    def test_aoc(cls):
        day = DAY
        url = URL.format(year=LONG_YEAR, day=day)
        request_day = day[1:] if day.startswith('0') else day
        
        assert cls.get_chrome_cookies()
        assert cls.get_firefox_cookies()
        assert cls.get_edge_cookies()
        assert cls.get_token()
        assert cls.make_request(method='GET', url=url)
        assert cls.get_story_input(year=YEAR, day=day)
        #assert cls.submit_answer(year=LONG_YEAR, day=request_day, title=TITLE, level=LEVEL_A, answer=PART_1)
        #assert cls.submit_answer(year=LONG_YEAR, day=request_day, title=TITLE, level=LEVEL_B, answer=PART_2)
        return 'Passed AOC tests!'
    
    @classmethod
    def test_methods(cls):
        cls.test_solver_functions()
        # cls.test_display() # testing in progress
        # cls.test_aoc()  # keep it commented to reduce amount of requests!

        return
        