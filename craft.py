#!/usr/bin/env python
# encoding: utf-8

from mcpi.minecraft import Minecraft

# rpi_address = "10.10.100.229"


class MineCraft:
    def __init__(self, address):
        self.id = 'minecraft'
        self.mc = Minecraft.create(address=address)

    def move_forward(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x+step, y, z)
        return {"id": self.id, "topic": "actuator"}

    def move_backward(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x-step, y, z)
        return {"id": self.id, "topic": "actuator"}

    def move_down(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x, y-step, z)
        return {"id": self.id, "topic": "actuator"}

    def move_up(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x, y+step, z)
        return {"id": self.id, "topic": "actuator"}

    def move_right(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x, y, z+step)
        return {"id": self.id, "topic": "actuator"}

    def move_left(self, step):
        step = int(step)
        x, y, z = self.mc.player.getPos()
        self.mc.player.setPos(x, y, z-step)
        return {"id": self.id, "topic": "actuator"}

    def say(self, word):
        self.mc.postToChat(word)
        return {"id": self.id, "topic": "actuator"}

    def is_connected(self, fuzz):
        if self.mc:
            return {"id": self.id, "topic": "sensor", "is_connected": True}
        else:
            return {"id": self.id, "topic": "sensor", "is_connected": False}

    def match(self):
        env = {
            'forward': self.move_forward,
            'backward': self.move_backward,
            'left': self.move_left,
            'right': self.move_right,
            'up': self.move_up,
            'down': self.move_down,
            'say': self.say,
            'is_connected': self.is_connected
        }
        return env
