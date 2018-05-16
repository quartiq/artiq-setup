import argparse

from migen.genlib.io import DifferentialOutput
from migen.build.generic_platform import ConstraintError

from misoc.integration.builder import builder_args, builder_argdict
from misoc.targets.kasli import soc_kasli_args, soc_kasli_argdict

from artiq.gateware.targets.kasli import Opticlock
from artiq.gateware import rtio
from artiq.gateware.rtio.phy import ttl_simple, ttl_serdes_7series, spi2
from artiq.build_soc import build_artiq_soc


class PTBHuntemann(Opticlock):
    def __init__(self, hw_rev=None, **kwargs):
        if hw_rev is None:
            hw_rev = "v1.1"
        Opticlock.__init__(self, hw_rev=hw_rev, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description="ARTIQ device binary builder for Kasli systems")
    builder_args(parser)
    soc_kasli_args(parser)
    parser.set_defaults(output_dir="artiq_kasli")
    args = parser.parse_args()

    soc = PTBHuntemann(**soc_kasli_argdict(args))
    build_artiq_soc(soc, builder_argdict(args))


if __name__ == "__main__":
    main()
