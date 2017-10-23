# Cubesat Comms System

## Setup
* Setup the RFM69 library via the instructions at
  [github.com/LowerPowerLab/RFM69](https://github.com/LowPowerLab/RFM69)
* Clone the CUbesat repo: `git clone https://github.com/columbiaspace/CUbesat`
* Open the files in the directory `CUbesat/comms/` to get started.


## Current System
* The current system closely follows the RFM69 Node and Gateway setup, but can be readily expanded to support sending arbitrary messages with full encryption.
* The setup is made to work with the [RFM69HCW](https://www.adafruit.com/product/3071) radio chip.

## Subdirectories
* Cubesat - Code to handle communication from the cubesat to a station
* Station - Code for communication with the cubesat and testing functionality
* The directories rf69\_client and rf69\_server have been kept for potential
  further development or integration. They employ a different RFM69 library.

## Contributing

Feel free to open an issue if you have an idea or feature request. To contribute code simply open a pull request.