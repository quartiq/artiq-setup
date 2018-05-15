import numpy as np
from artiq.experiment import *


class Demo(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("led0")

        for ch in range(24):
            self.setattr_device("ttl{}".format(ch))

        self.setattr_device("sampler0")

        for u in range(3):
            self.setattr_device("urukul{}_cpld".format(u))
            for ch in range(4):
                self.setattr_device("urukul{}_ch{}".format(u, ch))

        self.setattr_device("zotino0")

    @rpc(flags={"async"})
    def monitor(self, n, v):
        print(n, v)

    @kernel
    def run(self):
        self.core.break_realtime()
        delay(100*ms)
        self.sampler0.init()
        self.zotino0.init()
        while True:
            self.pulse_ttls(10*us)
            n = [0] * 4
            self.count_ttls(n)
            delay(100*us)
            v = [0.] * 8
            self.sampler0.sample(v)
            self.monitor(n, v)
            delay(500*ms)
            self.set_urukul()
            delay(15*ms)
            self.set_dacs()

    @kernel
    def set_urukul(self):
        self.urukul0_ch0.set_att(10*dB)
        self.urukul0_ch1.set_att(10*dB)
        self.urukul0_ch2.set_att(10*dB)
        self.urukul0_ch3.set_att(10*dB)
        self.urukul1_ch0.set_att(10*dB)
        self.urukul1_ch1.set_att(10*dB)
        self.urukul1_ch2.set_att(10*dB)
        self.urukul1_ch3.set_att(10*dB)
        self.urukul2_ch0.set_att(10*dB)
        self.urukul2_ch1.set_att(10*dB)
        self.urukul2_ch2.set_att(10*dB)
        self.urukul2_ch3.set_att(10*dB)
        self.urukul0_ch0.set(100*MHz)
        self.urukul0_ch1.set(110*MHz)
        self.urukul0_ch2.set(120*MHz)
        self.urukul0_ch3.set(130*MHz)
        self.urukul1_ch0.set(200*MHz)
        self.urukul1_ch1.set(210*MHz)
        self.urukul1_ch2.set(220*MHz)
        self.urukul1_ch3.set(230*MHz)
        self.urukul2_ch0.set(300*MHz)
        self.urukul2_ch1.set(310*MHz)
        self.urukul2_ch2.set(320*MHz)
        self.urukul2_ch3.set(330*MHz)
        self.urukul0_cpld.cfg_sw(0, 1)
        self.urukul0_cpld.cfg_sw(1, 1)
        self.urukul0_cpld.cfg_sw(2, 1)
        self.urukul0_cpld.cfg_sw(3, 1)
        self.urukul1_cpld.cfg_sw(0, 1)
        self.urukul1_cpld.cfg_sw(1, 1)
        self.urukul1_cpld.cfg_sw(2, 1)
        self.urukul1_cpld.cfg_sw(3, 1)
        self.urukul2_cpld.cfg_sw(0, 1)
        self.urukul2_cpld.cfg_sw(1, 1)
        self.urukul2_cpld.cfg_sw(2, 1)
        self.urukul2_cpld.cfg_sw(3, 1)

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
        self.ttl4.pulse(t)
        self.ttl5.pulse(t)
        self.ttl6.pulse(t)
        self.ttl7.pulse(t)
        self.ttl8.pulse(t)
        self.ttl9.pulse(t)
        self.ttl10.pulse(t)
        self.ttl11.pulse(t)
        self.ttl12.pulse(t)
        self.ttl13.pulse(t)
        self.ttl14.pulse(t)
        self.ttl15.pulse(t)
        self.ttl16.pulse(t)
        self.ttl17.pulse(t)
        self.ttl18.pulse(t)
        self.ttl19.pulse(t)
        self.ttl20.pulse(t)
        self.ttl21.pulse(t)
        self.ttl22.pulse(t)
        self.ttl23.pulse(t)

    @kernel
    def set_dacs(self):
        self.zotino0.set_leds(0xff)
        self.zotino0.set_dac(
            [-9. + i*.5 for i in range(32)],
            list(range(32))
        )
