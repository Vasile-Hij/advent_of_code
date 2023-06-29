from src.aoc.aoc_client import get_chrome_cookies, get_cookies, get_response, get_cached_html


assert get_chrome_cookies()
assert get_cookies()
assert get_response(2022, 3)
assert get_cached_html(2022, 5)
