from flask import Flask, render_template, redirect, request
import re, math

def clean_integer(text):
    """make sure no extraneous characters have been entered"""
    if not re.match("[0-9]+$", text) or re.match("[0]+$", text):
        return False
    return text

def is_prime(num):
    """returns True if num is prime"""
    count = 0
    for i in range(num):
        if (num % (i + 2)) == 0:
            count += 1
            if count > 1:
                return False
    return True

def is_fibonacci(num):
    return bool(is_square(5*num*num + 4) or is_square(5*num*num -4))

def is_square(num):
    max = round((num ** 0.5) + 1)
    return any(i * i == num for i in range(max))

def is_cube(num):
    max = round((num ** (1/3)) + 1)
    return any(i * i * i == num for i in range(max))

def factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def is_triangular(num):
    if num in [0, 1]:
        return True
    triangular_sum = 0
    for i in range(num):
        triangular_sum += i
        if triangular_sum == num:
            return True
        if triangular_sum > num or i == num:
            return False
