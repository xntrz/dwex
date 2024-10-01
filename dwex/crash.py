import hashlib, urllib, random, string, traceback, sys, os, platform
from urllib.request import urlopen
# No dependencies on the rest of the app, and keep it that way

_binary_desc = None

def set_binary_desc(s):
    global _binary_desc
    _binary_desc = s

def report_crash(exc, tb, version, catchpoint = None, ctxt=None):
    try:
        subj = '[python][dwex][pyexception]'
        if not catchpoint:
            subj += '[crash]'
    except Exception:
        pass

if __name__ == "__main__":
    try:
        def bar():
            i=0
            a=1
            a /=i

        def foo():
            bar()

        foo()
    except Exception as exc:
        from inspect import currentframe
        report_crash(exc, exc.__traceback__, (0, 50), currentframe())
