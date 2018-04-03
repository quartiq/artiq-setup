# Sinara

The Sinara components are open hardware. The designs are available under the
terms of the CERN Open Hardware License v1.2
(https://www.ohwr.org/attachments/2390/cern_ohl_v_1_2.pdf) at:
https://github.com/sinara-hw/sinara

The device has been configured with the software versions below.
An example device database, startup, idle, and demo experiments, as well
as this document are available at:
https://github.com/quartiq/artiq-setup/tree/ptb-schmidt

Modification and disassembly of the crate must only be done with proper ESD
protection and with the devices disconnected. Modifications that go beyond the
manipulation of the DIP switches or addition/removal of modules by qualified
personnel will void the warranty.

The controller and the modules are electrically floating and not connected
to mains ground via the power supply. A proper ground connection should be
established at an appropriate place.

# Components

## Controller

* Kasli/v1.1
* Serial: #21
* EUI-48: 54-10-ec-a9-d2-e0
* MAC: 54:10:ec:a9:d2:e0
* IP address: 10.0.16.30
* Gateware, bootloader, firmware: artiq-4.0.dev-efbe915b

## EEM0

* DIO_BNC/v1.2
* EUI-48: 54-10-ec-aa-1e-f7
* Channels 0-3: input
* Channels 4-7: output
* Termination: none

## EEM1

* DIO_BNC/v1.2
* EUI-48: 54-10-ec-a9-f7-b5
* Channels 0-3: output
* Channels 4-7: output
* Termination: none

## EEM4, EEM5

* Urukul-AD9910/v1.1
* EUI-48: 54-10-ec-35-06-c5, 54-10-ec-34-f0-a7
* 100 MHz XO on clk_sel=0
* using EEM1 for SW[0:3]

## EEM6

* Urukul-AD9912/v1.1
* EUI-48: 54-10-ec-35-75-57
* 100 MHz XO on clk_sel=0

## EEM7

* Zotino/v1.1
* EUI-48: 54-10-ec-aa-da-7c
