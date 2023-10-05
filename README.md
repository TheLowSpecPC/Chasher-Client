# Chasher Client

### Pinout
#### Raspberry Pi Pico
![](https://github.com/Saket-Upadhyay/PiPicoRFID/blob/main/docs/Pico-R3-A4-Pinout.png)
[SRC:https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
#### RC522 RFID Module
![](https://github.com/Saket-Upadhyay/PiPicoRFID/blob/main/docs/RC522-RFID-CARD-READERS-Pinout.png)
[SRC:https://microcontrollerslab.com/wp-content/uploads/2020/01/RC522-RFID-CARD-READERS-Pinout.png](https://microcontrollerslab.com/wp-content/uploads/2020/01/RC522-RFID-CARD-READERS-Pinout.png)

### Hardware Connection (RC522 to Pico)

| **RC522 RFID Reader Module**        | **Raspberry Pi Pico**        |
|-------------------------------------|------------------------------|
|     VCC                             |     3.3V                     |
|     RST                             |     GP0                      |
|     GND                             |     GND                      |
|     IRQ                             |     Not connected            |
|     MISO                            |     GP4                      |
|     MOSI                            |     GP3                      |
|     SCK                             |     GP2                      |
|     SDA                             |     GP1                      |

#### Set-up MicroPython in Pico
To set-up Pico with micropython [READ THIS PDF](https://github.com/Saket-Upadhyay/PiPicoRFID/blob/main/docs/raspberry-pi-pico-python-sdk.pdf)

`source : https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf (27 May 2022, 20:10 IST)`
