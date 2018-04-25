# Sinara

The Sinara components are open hardware. The designs are available under the
terms of the CERN Open Hardware License v1.2
(https://www.ohwr.org/attachments/2390/cern_ohl_v_1_2.pdf) at:
https://github.com/sinara-hw/sinara

The device has been configured with the software versions below.
An example device database, startup, idle, and demo experiments, as well
as this document are available at:
https://github.com/quartiq/artiq-setup/tree/hub-krutzik

Modification and disassembly of the crate must only be done with proper ESD
protection and with the devices disconnected. Modifications that go beyond the
manipulation of the DIP switches or addition/removal of modules by qualified
personnel will void the warranty.

The controller and the modules are electrically floating and not connected
to mains ground via the power supply. A proper ground connection should be
established at an appropriate place.

# Example setup sequence

Your control system is using a current development release (the `master` branch)
of ARTIQ (see below). Follow the guidelines in the `master` version of the manual
(https://m-labs.hk/artiq/manual-master/installing.html). As described in the
manual, a few steps are necessary to use the master branch.

To install the ARTIQ packages, both the `main` and the `dev` conda labels need
to be available. Insert the `dev` label between the `main` and the
`conda-forge` channels:

```
$ conda config --prepend channels http://conda.anaconda.org/conda-forge/label/main
$ conda config --prepend channels http://conda.anaconda.org/conda-forge/label/dev
$ conda config --prepend channels http://conda.anaconda.org/m-labs/label/main
```

Create and activate a conda environment for the exact ARTIQ package
release matching the gateware and software on your device:

```
$ conda create -n artiq-4 artiq=4.0.de=822+git1ef673c2
```

Clone this repository containing the device database and example experiments:

```
$ git clone -b hub-krutzik https://github.com/quartiq/artiq-setup.git
```

Activate the conda environment, and start an ARTIQ session using the examples:

```
$ activate artiq-4
$ cd artiq-setup
$ artiq_session
```

# Components

## Controller

* Kasli/v1.1
* Serial: #15
* EUI-48: 54-10-ec-a9-d2-7b
* MAC: 54:10:ec:a9:d2:7b
* IP address: 10.0.16.30
* Gateware, bootloader, firmware: artiq-4.0.dev 1ef673c2

## EEM0

* DIO_BNC/v1.1
* EUI-48:
* Channels 0-3: input
* Channels 4-7: output
* Termination: none

## EEM1

* DIO_BNC/v1.1
* EUI-48: d8-80-39-ee-f2-a4
* Channels 0-3: output
* Channels 4-7: output
* Termination: none

## EEM2

* DIO_BNC/v1.1
* EUI-48: d8-80-39-ef-43-2e
* Channels 0-3: output
* Channels 4-7: output
* Termination: none

## EEM3

* Sampler/v2.0
* EUI-48: 54-10-ec-36-83-cf
* Termination: none

## EEM4

* Urukul-AD9910/v1.1
* EUI-48: 54-10-ec-35-26-25
* 100 MHz XO on clk_sel=0

## EEM5

* Urukul-AD9910/v1.1
* EUI-48: 54-10-ec-35-62-e4
* 100 MHz XO on clk_sel=0

## EEM6

* Urukul-AD9910/v1.1
* EUI-48: 54-10-ec-35-06-70
* 100 MHz XO on clk_sel=0

## EEM7

* Zotino/v1.1
* EUI-48: 54-10-ec-a9-63-ed
* CH0-CH7 on IDC-BNC
