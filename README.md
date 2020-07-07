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
parameter：
```python
BarLine(line, color=None, size=None, font=None)
newline(line, color=None, size=None, font=None, bash=None, terminal=None, href=None)
submenusHead(line, color=None, size=None, font=None)
submenus(line, color=None, size=None, font=None, bash=None, terminal=None, href=None)
show()
```

href=.. to make the item clickable

color=.. to change their text color. eg. color=red or color=#ff0000

font=.. to change their text font. eg. font=UbuntuMono-Bold

size=.. to change their text size. eg. size=12

bash=.. to make the item run a given script terminal with your script e.g. bash=/Users/user/BitBar_Plugins/scripts/nginx.restart.sh if there are spaces in the file path you will need quotes e.g. bash="/Users/user/BitBar Plugins/scripts/nginx.restart.sh"

terminal=.. start bash script without opening Terminal. true or false

