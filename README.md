# PythonEnum
Enum class for python 2.7.

## Usage

To create an enum, the attributes must be in CAPITAL LETTERS and cannot start with '_'.
The attribute `_zero_value` is used to return false in `if` statement.

###### Basic example, with `_zero_value`
```
from enum import Enum

class NoYes(Enum):
    NO = 'No'
    YES = 'Yes'
    
    _zero_value = 'No'


yes = NoYes.YES

if yes:
    print ('The _zero_value is working')

if yes == NoYes.YES or yes == NoYes.from_value('Yes'):
    print ('This is another way to compare the values')

print (repr(yes))       # <EnumValue (NoYes.YES)>
print (yes)             # Yes
print (yes.value)       # Yes
print (yes.name)        # YES
print (yes.class_name)  # NoYes
```

###### Example without `_zero_value`, but with empty string
```
from enum import Enum

class Choices(Enum):
    EMPTY = ''
    LEFT = 'The left'
    RIGHT = 'The right'

empty = Choices.EMPTY
right = Choices.RIGHT

if not empty:
    print ('The value is EMPTY')

if right:
    print ('The value is not EMPTY')

if right == Choices.RIGHT:
    print ('The RIGHT choice')
```

###### Example without `_zero_value`, but with integer
```
from enum import Enum

class Options(Enum):
    NONE = 0
    ONE = 1
    TWO = 2

none = Options.NONE
two = Options.TWO

if not none:
    print ('The value is ZERO')

if two:
    print ('The value is not ZERO')

if two == Options.TWO:
    print ('The value is TWO')
```
