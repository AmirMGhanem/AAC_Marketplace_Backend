# AAC_Marketplace_Backend

git clone 
# macOS/Linux
You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
```python3 -m venv venv```

Activate Venv:
```. venv/bin/activate```
after venv is activated,

``` pip install -r requirements.txt ```

``` uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload ```
venv is virtual environment. and its in git ignore.

you may have to upgrade pip before installing the requirements.
if so, then usev
```pip install --upgrade pip```

****************************************************************

Mongo local
studio3t