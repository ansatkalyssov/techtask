## Technical Task

##### * Python 3.5.3+ required

##### Navigate to the project directory and create virtual environment


python -m venv venv

##### Activate it

source venv/bin/activate

##### Install Database

sqlite3 db.sqlite3

##### Install dependencies

pip install -r requirements.txt

##### options are:

-u --urls : urls to download separated by space.  
-f --file : path to text file with urls separated by ";", "," or new line.  
-n --number : number of simultaneous downloads, default 1.

##### For example

./downloader.py -f files.txt -n 2