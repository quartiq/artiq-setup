# Sinara

The Sinara components are open hardware. The designs are available under the
terms of the CERN Open Hardware License v1.2
(https://www.ohwr.org/attachments/2390/cern_ohl_v_1_2.pdf) at:
https://github.com/sinara-hw/sinara

# ARTIQ

ARTIQ is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

ARTIQ is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with ARTIQ. If not, see <http://www.gnu.org/licenses/>.

The ARTIQ source code is available at https://github.com/m-labs/artiq

# Code

The device has been configured with the software versions below.
An example device database, startup, idle, and demo experiments, as well
as this document are available at:
https://github.com/quartiq/artiq-setup/tree/luh-ospelkaus-18

# Electrical

Modification and disassembly of the crate must only be done with proper ESD
protection and with the devices disconnected. Modifications that go beyond the
manipulation of the DIP switches or addition/removal of modules by qualified
personnel will void the warranty.

The controller and the modules are electrically floating and not connected
to mains ground via the power supply. A proper ground connection should be
established at an appropriate place.

# Thermal

The crate needs unrestricted airflow for cooling. Keep the bottom and top
surfaces clear. In a rack leave 1U below and 1U above unused or use a [fan](https://www.reichelt.de/Zubehoer-Schaltschrankgehaeuse/LOGILINK-FAU02FG/3/index.html?ARTICLE=161905) [tray](https://www.digikey.de/product-detail/en/orion-fans/OA300ST-230/1053-1428-ND/2658718).

# Components

## Controller

* Kasli/v1.1
* Serial: #18
* IP address: 10.0.16.118
* Gateware, bootloader, firmware: artiq-4.0.dev 26faaad2

## EEM0

* DIO_BNC/v1.1
* Channels 0-3: input
* Channels 4-7: output
* Termination: none

## EEM1

* DIO_BNC/v1.1
* Channels 0-3: output
* Channels 4-7: output
* Termination: none

## EEM2

* DIO_BNC/v1.1
* Channels 0-3: output
* Channels 4-7: output
* Termination: none

## EEM3

* Sampler/v2.0
* Termination: none

## EEM4

* Urukul-AD9910/v1.1
* 100 MHz XO on clk_sel=0
* RF outputs and CLK SMA grounded

## EEM5

* Urukul-AD9910/v1.1
* 100 MHz XO on clk_sel=0
* RF outputs and CLK SMA grounded

## EEM6

* Grabber/v1.1

## EEM7

* Zotino/v1.1
