from src.aoc.aoc_client import AdventOfCodeBase
from src.common.display import Display


_source = 'say hello, to my little friend! Codename_47-2002'
_source_multilines = 'say hello, to my little friend!\nCodename_47-2002'
_year, _day = '2022', '3'
_year_long, _request_day = _year, _day
_title = 'Codename 47'
_display = 10


class Test(Display, AdventOfCodeBase):
    @classmethod
    def test_solver_functions(cls):
        # print(cls.read_raw('.setup.cfg'))
        # print(cls.write_file('delete_this'))

        assert cls.make_list(str, _source) == ['s', 'a', 'y', ' ', 'h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'o', ' ', 'm', 'y', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 'f', 'r', 'i', 'e', 'n', 'd', '!', ' ', 'C', 'o', 'd', 'e', 'n', 'a', 'm', 'e', '_', '4', '7', '-', '2', '0', '0', '2']
        assert cls.make_tuple(str, _source) == ('s', 'a', 'y', ' ', 'h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'o', ' ', 'm', 'y', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 'f', 'r', 'i', 'e', 'n', 'd', '!', ' ', 'C', 'o', 'd', 'e', 'n', 'a', 'm', 'e', '_', '4', '7', '-', '2', '0', '0', '2')

        assert cls.str_split(_source) == ['say', 'hello,', 'to', 'my', 'little', 'friend!', 'Codename_47-2002']
        assert cls.str_strip(_source) == 'say hello, to my little friend! Codename_47-2002'
        assert cls.paragraph(_source) == ['say hello, to my little friend! Codename_47-2002']

        assert cls.each_first_item(_year) == ['2', '0', '2', '2']
        assert cls.each_item(_year) == ['2', '0', '2', '2']
        assert cls.check_len_string(_source) is True
        assert cls.strings_per_line(_source_multilines) == ['say hello, to my little friend!', 'Codename_47-2002']

        assert cls.truncate(obj='say hello', width=99) == 'say hello'
        assert cls.truncate(obj='say hello', width=7) == 'say ...'

        assert cls.integers(_source) == (47, -2002)
        assert cls.positive_integers(_source) == (47, 2002)
        assert cls.find_digits(_source) == (4, 7, 2, 0, 0, 2)
        assert cls.find_strings(_source) == ('say', 'hello', 'to', 'my', 'little', 'friend', 'Codename')
        return
    
    #@classmethod
    # def test_display(cls):
    #     assert cls.helper_base(
    #         source=_source, 
    #         year=_year, 
    #         title=_title,
    #         display_type='paragraph',
    #         parser_method='integers',
    #         display=_display
    #     ) == ('say', 'hello')
    #     assert cls.helper_base(
    #         source=_source_multilines, 
    #         year=_year, 
    #         title=_title,
    #         display_type='paragraph',
    #         parser_method='find_digits',
    #         display=_display
    #     ) == ((1, 2, 3), (7,))
    # 
    #     return

    @classmethod
    def test_aoc(cls):
        assert cls.get_chrome_cookies()
        assert cls.get_cookies()
        assert cls.get_response(year=_year, day=_day)
        assert cls.get_cached_html(year=_year, day=_day, year_long=_year_long, request_day=_request_day)

        return
    
    @classmethod
    def test_methods(cls):
        cls.test_solver_functions()
        # cls.test_display() # testing in progress
        # cls.test_aoc()  # keep it commented to reduce amount of requests!

        return
        