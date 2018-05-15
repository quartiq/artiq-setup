from artiq.experiment import *


class Startup(EnvExperiment):
    def build(self):
        self.setattr_device("core")

        for u in range(3):
            self.setattr_device("urukul{}_cpld".format(u))
            for ch in range(4):
                self.setattr_device("urukul{}_ch{}".format(u, ch))

        self.setattr_device("zotino0")
        self.setattr_device("sampler0")

        self.setattr_device("led0")

    @kernel
    def run(self):
        self.core.reset()

        delay(20*ms)
        self.sampler0.init()
        # set all channels to default as well
        self.sampler0.set_gain_mu(0, 0)

        delay(20*ms)
        self.urukul0_cpld.init()
        delay(20*ms)
        self.urukul0_ch0.init()
        self.urukul0_ch1.init()
        self.urukul0_ch2.init()
        self.urukul0_ch3.init()

        delay(20*ms)
        self.urukul1_cpld.init()
        delay(20*ms)
        self.urukul1_ch0.init()
        self.urukul1_ch1.init()
        self.urukul1_ch2.init()
        self.urukul1_ch3.init()

        delay(20*ms)
        try:
            self.urukul2_cpld.init()
            delay(20*ms)
            self.urukul2_ch0.init()
            self.urukul2_ch1.init()
            self.urukul2_ch2.init()
            self.urukul2_ch3.init()
        except:  # grabber
            pass

        delay(20*ms)
        self.zotino0.init()

        delay(10*ms)
        for i in range(3):
            self.led0.pulse(.1*s)
            self.led0.sync()
            delay(.1*s)
