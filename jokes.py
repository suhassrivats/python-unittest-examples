import requests

def get_joke():
	url = 'https://api.chucknorris.io/jokes/random'

	try:
		response = requests.get(url, timeout=30)
		response.raise_for_status()

	except requests.exceptions.Timeout:
		return 'Timeout. Could not fetch jokes'

	except requests.exceptions.ConnectionError:
		pass

	except requests.exceptions.HTTPError:
		return 'HTTPError was raised'

	else:
		if response.status_code == 200:
			joke = response.json()['value']
		else:
			joke = 'No jokes'

	return joke


def len_joke():
	joke = get_joke()
	# print(f'The length of joke \'{joke}\' is: {len(joke)}')
	return len(joke)


if __name__ == '__main__':
	print(get_joke)