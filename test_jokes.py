import unittest
from unittest.mock import patch, MagicMock
import requests
from requests.exceptions import Timeout, HTTPError

import jokes


class TestJoke(unittest.TestCase):

	@patch('jokes.get_joke')
	def test_len_joke(self, mock_get_joke):
		# mock_get_joke.return_value = 'one'
		mock_get_joke.side_effect = [
			'one',
			'two',
			'three'
		]

		self.assertEqual(jokes.len_joke(), 3)
		self.assertEqual(jokes.len_joke(), 3)
		self.assertEqual(jokes.len_joke(), 5)


	@patch('jokes.requests')
	def test_get_joke(self, mock_requests):

		mock_response = MagicMock()
		mock_response.status_code = 403
		mock_response.json.return_value = {'value': 'joke1'}

		mock_requests.get.return_value = mock_response

		self.assertEqual(jokes.get_joke(), 'No jokes')


	@patch('jokes.requests')
	def test_get_joke_timeout_exception(self, mock_requests):

		mock_requests.exceptions = requests.exceptions
		mock_requests.get.side_effect = Timeout('Seems the server is down')

		self.assertEqual(jokes.get_joke(), 'Timeout. Could not fetch jokes')


	@patch('jokes.requests')
	def test_get_joke_raise_for_status(self, mock_requests):

		mock_requests.exceptions = requests.exceptions

		mock_response = MagicMock()
		mock_response.status_code = 403
		mock_response.raise_for_status.side_effect = HTTPError('Something goes wrong')

		mock_requests.get.return_value = mock_response

		self.assertEqual(jokes.get_joke(), 'HTTPError was raised')

if __name__ == '__main__':
	unittest.main()