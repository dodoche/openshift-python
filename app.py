#!/usr/bin/python
from __future__ import print_function
from __future__ import absolute_import
import openshift as oc
from contextlib import contextmanager
import argparse
import time
import logging
import traceback
import selector
import model

def main():

  configmaps =  selector("configmaps")
  Configmaps = configmaps.objects()
  conf = Configmaps[2]
  print('Annotations:\n{}\n'.format(conf.model.metadata))

if __name__ == '__main__':
  main()
