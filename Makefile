SHELL := bash
include *.mk

.PHONY: test
test: compose-run