#!/usr/bin/env python
import sys, os
import logging
from logging.handlers import RotatingFileHandler
from configlog import configLogging

loggerModuleSingleton = None

def getLoggerModule():
  global loggerModuleSingleton
  if loggerModuleSingleton is None:
    loggerModuleSingleton = LoggerModule()
  return loggerModuleSingleton


class LoggerModule(object):
	def __init__(self):
		# Set up logging
		logging.basicConfig(level=logging.DEBUG)
		self.logger = logging.getLogger(__name__)
		configLogging(self.logger)