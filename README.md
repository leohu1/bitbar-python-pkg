bitbar
=================

bitbar-python

bitbar write with python

a python out put

Bar Line:

```python
from bitbar import BitBar


Bar = BitBar()
Bar.BarLine('η', color='cadetblue')
Bar.show()
```
New Line:
```python
from bitbar import BitBar


Bar = BitBar()
Bar.BarLine('η', color='cadetblue')
Bar.newline('a', color='green')
Bar.show()
```
Sub Menus:
```python
from bitbar import BitBar


Bar = BitBar()
Bar.BarLine('η', color='cadetblue')
Bar.newline('a', color='green')
Bar.submenusHead('b')
Bar.submenus('c', color='green')
Bar.show()
```
