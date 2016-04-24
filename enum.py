# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


class EnumValue(object):
    def __init__(self, name, value, class_name, is_zero=None):
        self.name = name
        self.value = value
        self.class_name = class_name
        self.is_zero = is_zero

    def __repr__(self):
        return '<EnumValue ({}.{})>'.format(self.class_name, self.name)

    def __str__(self):
        return str(self.value)

    def __nonzero__(self):
        if self.is_zero is not None:
            return not self.is_zero

        if type(self.value) in [str, unicode]:
            return len(self.value)

        if type(self.value) == int:
            return self.value

        return 0


class EnumType(type):
    def __new__(mcs, class_name, class_type, class_dict):
        zero_value = class_dict.get('_zero_value')
        for k, v in class_dict.iteritems():
            if not k.startswith('_') and type(v) in (str, int, unicode):
                is_zero = v == zero_value if zero_value is not None else None
                class_dict[k] = EnumValue(k, v, class_name, is_zero)

        return super(EnumType, mcs).__new__(mcs, class_name, class_type, class_dict)


class Enum(object):
    __metaclass__ = EnumType

    @classmethod
    def from_value(cls, value):
        for k, v in cls.__dict__.iteritems():
            if not k.startswith('_') and type(v) == EnumValue and v.value == value:
                return v

    @classmethod
    def to_dict(cls):
        return enum_to_dict(cls)


def enum_to_dict(enum):
    attributes = enum.__dict__
    ret = {}
    for key in attributes:
        attr = attributes[key]
        if isinstance(attr, EnumValue):
            ret[attr.name] = attr.value

    return ret
