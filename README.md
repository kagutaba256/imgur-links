# getting imgur links from album with BeautifulSoup

this wont work forever but it works for now.

## Usage

you will need to install BeautifulSoup and requests

```console
pip install beautifulsoup4 requests --user
```

then run the script with the album url and the path to the file you want to save the links to

```console
python imgur-soup.py <album url> <path to file for links>
```

for instance
```console
python imgur-soup.py http://imgur.com/a/8ZaYF links.txt
```
