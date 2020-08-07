# Simple Quiz App with wxPython

## Installation
* Create virtual environment with `python -m venv venv`
* Activate `venv` with `source venv/bin/activate`
* Install all the requirements with `pip install -r requirements.txt`
* Launch app with `python main.py`
* Optionally, build an executable with [PyInstaller](https://www.pyinstaller.org/)

## Test format
Test is a simple text file (should be located within the same folder)
of the following format:
```
<Question 1>;<Correct answer>;<Answer 1>;<Answer 2>;<Answer 3>;<Answer 4>
<Question 2>;<Correct answer>;<Answer 1>;<Answer 2>;<Answer 3>;<Answer 4>
etc...
```
for example this will be one-question quiz 
```
Name?;0;Mike;Pike;Rob;Bob
```
For more examples, see *test1.txt*

## Notes
The *gui.fbp* file is a 
[wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder)
GUI description, we may use it to generate the *gui.py* module
