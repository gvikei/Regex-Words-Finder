## :smile: Welcome to Regex Words Finder :smile:

- Regex Words Finder (RWF) is a web app optimized for finding words with a provided set of characters and a pattern written in Regex form. It also return the score associated with the word, as given by the Words With Friends game on Facebook.

- Usage: 
   - Enter the letters **iootr** in the first box and the and the pattern **rep.si...y** in the second box, click "Get Words!", the app returns **repository: 15**.

### Routes
- `GET /`: Returns the content of the app
- `GET /words/<letters>`: Takes in a string of scrabble letters as a URI param and returns a JSON file with resulting scrabble words

### Build Instructions
1. Download and install [Python 3.5](https://www.python.org/downloads/release/python-350/)
2. Clone this repository to your machine
3. Open a terminal and change into the root of the repository
4. Install virtualenv `pip install virtualenv`
5. Create a virtual environment `virtualenv venv`
6. Activate the virtual environment `source venv/bin/activate`
7. Install dependencies `pip install -r requirements.txt`

### Running the server
- Run `python start_server.py`

### Running the tests
- Run `py.test tests`

### Implementation Details
- TBD.
