# piano-spider

This is a library of a web-crawler to craw information from several local piano website to get their listing information.

## Setup
```bash
# configure conda environment
conda create -n piano-spider
conda activate piano-spider
conda pip install pip
pip install -r requirements.txt
```

Dev guide
```shell
# tools to interative development
PYTHON_HOME=ipython scrapy shell 'https://seattle.classicpianos.net/new-pianos/yamaha'
```

## Usage
```bash
# crawl piano information
scrapy crawl pianos

# after saving information to pianos.db
sqlite3 db/pianos.db

# querying from db
sqlite> .tables
pianos
sqlite> select count(*) from pianos;
30
```


