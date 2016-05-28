#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import crosys
import platform
import site
import sys
import os
import six

SP_PATH = os.path.dirname(six.__file__)

def test_all():
    assert crosys.SP_PATH == SP_PATH


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")