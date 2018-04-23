from artiq.experiment import *


class Idle(EnvExperiment):
    def build(self):
        self.setattr_device("core")

        self.setattr_device("led0")

    @kernel
    def run(self):
        self.core.break_realtime()

        delay(1*us)
        for i in range(10):
            self.led0.pulse(.5*s)
            self.led0.sync()
            delay(.5*s)
