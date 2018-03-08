from artiq.experiment import *


class Idle(EnvExperiment):
    def build(self):
        self.setattr_device("core")

        self.setattr_device("probe0")
        self.setattr_device("led0")
        self.setattr_device("cool0")

    @kernel
    def run(self):
        self.core.break_realtime()

        self.cool0.on()
        delay(1*us)
        self.probe0.sw.off()
        delay(1*us)
        for i in range(10):
            self.led0.pulse(.5*s)
            self.led0.sync()
            delay(.5*s)
