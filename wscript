#! /usr/bin/env python
# encoding: utf-8

APPNAME = "unity"
VERSION = "3.0.0"


def configure(ctx):

    ctx.load("cmake")

    if ctx.is_toplevel():
        ctx.cmake_configure()


def options(ctx):
    ctx.load("cmake")


def build(ctx):

    ctx.load("cmake")

    if ctx.is_toplevel():
        ctx.cmake_build()

