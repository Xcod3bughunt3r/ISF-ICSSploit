#!/usr/bin/env python2
# Created by Xcod3bughunt3r
# The MIT License (MIT).
# Copyright (c) 2022 ALIF-FUSOBAR.

import logging

LOGGER = logging.getLogger(__name__)

class icssploitException(Exception):
    def __init__(self, msg=''):
        super(icssploitException, self).__init__(msg)
        LOGGER.exception(self)

class OptionValidationError(icssploitException):
    pass

class StopThreadPoolExecutor(icssploitException):
    pass
