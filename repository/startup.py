from artiq.experiment import *


class Startup(EnvExperiment):
    def build(self):
        self.setattr_device("core")

        self.setattr_device("urukul0_cpld")
        for ch in range(4):
            self.setattr_device("urukul0_ch{}".format(ch))

        self.setattr_device("led0")

    @kernel
    def run(self):
        self.core.reset()

        delay(20*ms)
        self.urukul0_cpld.init()
        delay(20*ms)
        self.urukul0_ch0.init()
        self.urukul0_ch1.init()
        self.urukul0_ch2.init()
        self.urukul0_ch3.init()

        for i in range(3):
            self.led0.pulse(.1*s)
            self.led0.sync()
            delay(.1*s)
