import numpy as np
from artiq.experiment import *


class Demo(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("led0")

        for ch in range(8):
            self.setattr_device("ttl{}".format(ch))

        for u in range(1):
            self.setattr_device("urukul{}_cpld".format(u))
            for ch in range(4):
                self.setattr_device("urukul{}_ch{}".format(u, ch))

    @rpc(flags={"async"})
    def monitor(self, n):
        print("ttl_in: {}".format(n))

    @kernel
    def run(self):
        self.core.break_realtime()
        delay(100*ms)
        while True:
            self.pulse_ttls(10*us)
            n = [0] * 4
            self.count_ttls(n)
            delay(100*us)
            self.monitor(n)
            delay(500*ms)
            self.set_urukul()

    @kernel
    def set_urukul(self):
        self.urukul0_ch0.set_att(10*dB)
        self.urukul0_ch1.set_att(10*dB)
        self.urukul0_ch2.set_att(10*dB)
        self.urukul0_ch3.set_att(10*dB)
        self.urukul0_ch0.set(100*MHz)
        self.urukul0_ch1.set(110*MHz)
        self.urukul0_ch2.set(120*MHz)
        self.urukul0_ch3.set(130*MHz)
        self.urukul0_ch0.sw.on()
        self.urukul0_ch1.sw.on()
        self.urukul0_ch2.sw.on()
        self.urukul0_ch3.sw.on()

    @kernel
    def count_ttls(self, n):
        n[0] = self.ttl0.count()
        n[1] = self.ttl1.count()
        n[2] = self.ttl2.count()
        n[3] = self.ttl3.count()

    @kernel
    def pulse_ttls(self, t):
        t0 = now_mu()
        self.ttl0.gate_rising(t)
        self.ttl1.gate_rising(t)
        self.ttl2.gate_rising(t)
        self.ttl3.gate_rising(t)
        at_mu(t0)
        delay(t/10.)
        self.ttl4.pulse(t)
        self.ttl5.pulse(t)
        self.ttl6.pulse(t)
        self.ttl7.pulse(t)
