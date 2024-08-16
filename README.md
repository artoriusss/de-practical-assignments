# de-practical-assignments

```
git clone git@github.com:artoriusss/de-practical-assignments.git
```

```
cd de-practical-assignments
```

To run the code from this repository, please follow these steps (provided you're using a UNIX-based system):

Create a virtual environment using `uv` (replace `uv` with `python -m venv .venv` and avoid typing `uv` in all of the subsequent commands if you want to use a regular package manager).

```
uv venv
```
Activate a virtual environment:
```
source .venv/bin/activate
```
Finally, you need to install required dependencies:
```
uv pip install -r requirements.txt
```

Now you're ready to run code for practical assignements. You can do this with a command like this one:

```
python 1-numpy/t4.py
```