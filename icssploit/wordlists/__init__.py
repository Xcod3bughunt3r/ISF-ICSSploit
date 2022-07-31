#!/usr/bin/env python2
# Created by Xcod3bughunt3r
# The MIT License (MIT).
# Copyright (c) 2022 ALIF-FUSOBAR.

import pkg_resources

defaults = 'file://' + pkg_resources.resource_filename(__name__, 'defaults.txt')
passwords = 'file://' + pkg_resources.resource_filename(__name__, 'passwords.txt')
usernames = 'file://' + pkg_resources.resource_filename(__name__, 'usernames.txt')
snmp = 'file://' + pkg_resources.resource_filename(__name__, 'snmp.txt')
