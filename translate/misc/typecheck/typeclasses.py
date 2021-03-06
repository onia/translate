from translate.misc.typecheck import Typeclass

### Number
####################################################

_numbers = [int, float, complex, int, bool]
try:
    from decimal import Decimal
    _numbers.append(Decimal)
    del Decimal
except ImportError:
    pass
    
Number = Typeclass(*_numbers)
del _numbers
    
### String -- subinstance of ImSequence
####################################################

String = Typeclass(str, str)
    
### ImSequence -- immutable sequences
####################################################

ImSequence = Typeclass(tuple, range, String)

### MSequence -- mutable sequences
####################################################

MSequence = Typeclass(list)

### Mapping
####################################################

Mapping = Typeclass(dict)
