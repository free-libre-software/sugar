# Copyright (C) 2006, Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os
import sys
import pwd

try:
    from sugar.__uninstalled__ import *
except ImportError:
    from sugar.__installed__ import *

def _get_prefix_path(base, path=None):
    if os.environ.has_key('SUGAR_PREFIX'):
        prefix = os.environ['SUGAR_PREFIX']
    else:
        prefix = '/usr'

    if path:
        return os.path.join(prefix, base, path)
    else:
        return os.path.join(prefix, base)

def is_emulator():
    if os.environ.has_key('SUGAR_EMULATOR'):
        if os.environ['SUGAR_EMULATOR'] == 'yes':
            return True
    return False

def get_profile_path():
    if os.environ.has_key('SUGAR_PROFILE'):
        profile_id = os.environ['SUGAR_PROFILE']
    else:
        profile_id = 'default'

    path = os.path.join(os.path.expanduser('~/.sugar'), profile_id)
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError, exc:
            print "Could not create user directory."

    return path

def get_user_activities_path():
    path = os.path.expanduser('~/Activities')
    if not os.path.isdir(path):
        os.mkdir(path)
    return path

def get_bin_path(path=None):
    return _get_prefix_path('bin', path)

def get_service_path(name):
    return _get_prefix_path('share/sugar/services', name)

def get_shell_path(path=None):
    return _get_prefix_path('share/sugar/shell', path)

def get_emulator_path(path=None):
    return _get_prefix_path('share/sugar/emulator', path)
