import requests
import os
import sys

def fuzz_url(base_url, wordlist):
	wordlist_path = os.path.join(os.path.dirname(__file__), wordlist)
	try:
		with open(wordlist_path, "r") as file:
			words = file.read().splitlines()
		for word in words:
			url = f"{base_url}/{word}"
			response = requests.get(url)
			print(f"URL: {url}, Status Code: {response.status_code}")
	except  FileNotFoundError:
		print(f"Error: Wordlist file `{wordlist}` not found.")
	except requests.RequestException as e:
		print(f"Error making request: {e}")
	except KeyboardInterrupt:
		print(f"Fuzzing interrupted by user.")
		sys.exit(0)

if len(sys.argv) != 3:
	print("Usage: python script.py <base_url> <wordlist>")
	sys.exit(1)

base_url = sys.argv[1]
wordlist = sys.argv[2]

fuzz_url(base_url, wordlist)
