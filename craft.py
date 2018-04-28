#!/usr/bin/env python
# encoding: utf-8

from mcpi.minecraft import Minecraft
rpi_address = "10.10.100.139"

mc = Minecraft.create(address=rpi_address)


# while True:
#     mc.postToChat("Hello world")


def move_forward(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x+step, y, z)
    return


def move_backward(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x-step, y, z)
    return


def move_down(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y-step, z)
    return


def move_up(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y+step, z)
    return


def move_right(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y, z+step)
    return


def move_left(step):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y, z-step)
    return


match = {
    'forward': move_forward,
    'backward': move_backward,
    'left': move_left,
    'right': move_right,
    'up': move_up,
    'down': move_down
}
