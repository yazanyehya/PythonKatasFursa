import unittest
from typing import Dict
import re

# --- Reusing parse_log function here ---
def parse_log(log: str) -> Dict[str, str]:
    pattern = re.compile(
        r'(?P<client_ip>\S+)\s+-\s+-\s+'
        r'\[(?P<date>[^\]]+)\]\s+'
        r'"(?P<http_method>\S+)\s+(?P<path>\S+)\s+HTTP/(?P<http_version>[^"]+)"\s+'
        r'(?P<status>\d+)\s+(?P<response_bytes>\d+)\s+'
        r'"[^"]*"\s+"(?P<user_agent>[^"]+)"'
    )

    match = pattern.match(log)
    if not match:
        raise ValueError("Invalid log format")

    return match.groupdict()

# --- Unit test class ---
class TestParseLog(unittest.TestCase):

    def test_valid_log(self):
        log_entry = (
            '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
            '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
            '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
        )
        expected = {
            'client_ip': '122.176.223.47',
            'date': '05/Feb/2024:08:29:40 +0000',
            'http_method': 'GET',
            'path': '/web-enabled/Enhanced-portal/bifurcated-forecast.js',
            'http_version': '1.1',
            'status': '200',
            'response_bytes': '1684',
            'user_agent': 'Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00'
        }
        self.assertEqual(parse_log(log_entry), expected)

    def test_invalid_log_format(self):
        bad_log = 'this is not a valid log format'
        with self.assertRaises(ValueError):
            parse_log(bad_log)

    def test_missing_fields(self):
        # Missing user agent and response bytes
        bad_log = (
            '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
            '"GET /path HTTP/1.1" 200 '
            '"-" "-"'
        )
        with self.assertRaises(ValueError):
            parse_log(bad_log)


if __name__ == "__main__":
    unittest.main()
