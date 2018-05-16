import argparse

from migen.genlib.io import DifferentialOutput
from migen.build.generic_platform import ConstraintError

from misoc.integration.builder import builder_args, builder_argdict
from misoc.targets.kasli import soc_kasli_args, soc_kasli_argdict

from artiq.gateware.targets.kasli import (
    _StandaloneBase, _dio, _urukul, _sampler, _zotino)
from artiq.gateware import rtio
from artiq.gateware.rtio.phy import ttl_simple, ttl_serdes_7series, spi2
from artiq.build_soc import build_artiq_soc


class UFrWarring(_StandaloneBase):
    def __init__(self, hw_rev=None, **kwargs):
        if hw_rev is None:
            hw_rev = "v1.1"
        _StandaloneBase.__init__(self, hw_rev=hw_rev, **kwargs)

        self.config["SI5324_AS_SYNTHESIZER"] = None
        # self.config["SI5324_EXT_REF"] = None
        self.config["RTIO_FREQUENCY"] = "125.0"

        platform = self.platform
        platform.add_extension(_dio("eem0"))
        platform.add_extension(_urukul("eem5", "eem4"))

        try:
            # EEM clock fan-out from Si5324, not MMCX, only Kasli/v1.0
            self.comb += platform.request("clk_sel").eq(1)
        except ConstraintError:
            pass

        rtio_channels = []
        for i in range(8):
            eem, port = divmod(i, 8)
            pads = platform.request("eem{}".format(eem), port)
            if i < 4:
                cls = ttl_serdes_7series.InOut_8X
            else:
                cls = ttl_serdes_7series.Output_8X
            phy = cls(pads.p, pads.n)
            self.submodules += phy
            rtio_channels.append(rtio.Channel.from_phy(phy))

        # EEM5+EEM4: Urukul
        for eem in "eem5".split():
            phy = spi2.SPIMaster(self.platform.request("{}_spi_p".format(eem)),
                    self.platform.request("{}_spi_n".format(eem)))
            self.submodules += phy
            rtio_channels.append(rtio.Channel.from_phy(phy, ififo_depth=4))

            pads = platform.request("{}_dds_reset".format(eem))
            self.specials += DifferentialOutput(0, pads.p, pads.n)

            pads = platform.request("{}_io_update".format(eem))
            phy = ttl_serdes_7series.Output_8X(pads.p, pads.n)
            self.submodules += phy
            rtio_channels.append(rtio.Channel.from_phy(phy))

            for i in range(4):
                pads = platform.request("{}_sw{}".format(eem, i))
                phy = ttl_serdes_7series.Output_8X(pads.p, pads.n)
                self.submodules += phy
                rtio_channels.append(rtio.Channel.from_phy(phy))

        for i in (1, 2):
            sfp_ctl = platform.request("sfp_ctl", i)
            phy = ttl_simple.Output(sfp_ctl.led)
            self.submodules += phy
            rtio_channels.append(rtio.Channel.from_phy(phy))

        self.config["HAS_RTIO_LOG"] = None
        self.config["RTIO_LOG_CHANNEL"] = len(rtio_channels)
        rtio_channels.append(rtio.LogChannel())

        self.add_rtio(rtio_channels)


def main():
    parser = argparse.ArgumentParser(
        description="ARTIQ device binary builder for Kasli systems")
    builder_args(parser)
    soc_kasli_args(parser)
    parser.set_defaults(output_dir="artiq_kasli")
    args = parser.parse_args()

    soc = UFrWarring(**soc_kasli_argdict(args))
    build_artiq_soc(soc, builder_argdict(args))


if __name__ == "__main__":
    main()
