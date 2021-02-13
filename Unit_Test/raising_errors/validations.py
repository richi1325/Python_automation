#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def validate_user(username, minlen):
    assert type(username) == str, "Username must be a string"
    if minlen<1:
        raise ValueError("minlen parameter must be at least 1")
    if len(username)<minlen:
        return False
    if not username.isalnum():
        return False
    return True