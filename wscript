#! /usr/bin/env python
# encoding: utf-8

APPNAME = "unity"
VERSION = "3.0.0"


def build(bld):
    src = bld.dependency_node("unity-source").find_dir("src")

    bld.stlib(
        features="c",
        source=[src.find_resource("unity.c")],
        target="unity",
        includes=[src],
        export_includes=[src],
        use=[],
    )

    if bld.is_toplevel():
        bld.recurse("test")
