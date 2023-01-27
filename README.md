# getting imgur links from album with BeautifulSoup

this wont work forever but it works for now.

## Usage

you will need to install BeautifulSoup and requests

```shell
pip install beautifulsoup4 requests --user
```

then run the script with the album url and the path to the file you want to save the links to

```shell
python imgur.py <album url> <path to file for links>
```

for instance
```shell
python imgur.py http://imgur.com/a/8ZaYF links.txt
```
