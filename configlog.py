#!/usr/bin/env python
import sys, os
import logging
from logging.handlers import RotatingFileHandler




def configLogging(logger):
	# Set up logging
	#logging.basicConfig(level=logging.DEBUG)
	#logger = logging.getLogger(__name__)

	# setting log
	fh = RotatingFileHandler('debug.log', maxBytes=100000, backupCount=10)
	fh.setLevel(logging.DEBUG)
	fh2 = RotatingFileHandler('info.log', maxBytes=100000, backupCount=5)
	fh2.setLevel(logging.INFO)
	er = RotatingFileHandler('error.log', maxBytes=100000, backupCount=2)
	er.setLevel(logging.WARNING)
	ch = logging.StreamHandler(sys.stdout)
	ch.setLevel(1)
	# format logger
	fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	fh2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	er.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	ch.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(fh2)
	logger.addHandler(ch)
	logger.addHandler(er)

	logger.info("Logging configured.")