#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GAMADV-XTD3
#
# Copyright 2022, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import multiprocessing

import gam

def main():
  if sys.platform.startswith('win'):
    multiprocessing.freeze_support()
  if sys.platform == 'darwin':
    # https://bugs.python.org/issue33725 in Python 3.8.0 seems
    # to break parallel operations with errors about extra -b
    # command line arguments
    multiprocessing.set_start_method('fork')
  gam.initializeLogging()
  rc = gam.ProcessGAMCommand(sys.argv)
  try:
    sys.stdout.flush()
  except (IOError, ValueError):
    pass
  sys.exit(rc)

# Run from command line
if __name__ == '__main__':
  main()
