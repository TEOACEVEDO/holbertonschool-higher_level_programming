#!/usr/bin/python3
class LockedClass:
    """We use __slots__ to prevent the user from dynamically creating new instance attributes"""
    __slots__ = 'first_name'
