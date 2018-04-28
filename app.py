#!/usr/bin/env python
# encoding: utf-8

from mcpi.minecraft import Minecraft
rpi_address = "10.10.100.155"
mc = Minecraft.create(address = rpi_address)
mc.postToChat("Hello world")

