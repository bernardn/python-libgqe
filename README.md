# python-libgqe

A library for interfacing [GQ Electronics](http://www.gqelectronicsllc.com/comersus/store/comersus_dynamicIndex.asp?idAffiliate=7394) radiation measurement devices.

## Protocols

The following protocols have been implemented :
- [GQ-RFC1201](doc/GQ-RFC1201.txt)
- [GQ-RFC1701](doc/GQ-RFC1701.txt)
- [GQ-RFC1801](doc/GQ-RFC1801.txt)

## Units

The following device units have been TESTED with this software :

### EMF meters
- [GQEMF-390](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5678)


The following device units have been implemented in this software:

### EMF meters
- [GQEMF-360](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5682)
- GQEMF-360+
- GQEMF-380
- [GQEMF-390](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5678)

### Geiger-Müller counters
- [GMC-500](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5629)
- [GMC-500+](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5631)
- GMC-600
- [GMC-600+](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=5637)

The following device units will probably some day be implemented in this software:

### Geiger-Müller counters

- GMC-280
- GMC-300
- GMC-300+
- GMC-320
- [GMC-320+](https://www.gqelectronicsllc.com/comersus/store/comersus_viewItem.asp?idAffiliate=7394&idProduct=4579)

## Quick start

`$ gqe-cli --help`

`$ gqe-cli  /dev/tty.wchusbserialfd120  --help`

`$ gqe-cli  /dev/tty.wchusbserialfd120 --unit GQEMF390 --revision 'Re 2.51' --help`

Replace `/dev/tty.wchusbserialfd120` with the path to the COM RS232 interface the unit is connected to.

## Example for GQEMF-390

```
$ ./gqe-cli /dev/tty.wchusbserialfd120 --help
usage: gqe-cli [--unit UNIT] [--revision REVISION] [--out-file OUT_FILE]
               [--in-file IN_FILE] [--format FORMAT] [--help] [--echo ECHO]
               [--get-battery-voltage] [--get-cfg] [--get-dsid] [--get-ef]
               [--get-emf] [--get-gyroscope] [--get-identity] [--get-mode]
               [--get-rf GET_RF] [--get-screen] [--get-serial] [--get-xyz]
               [--key-hold KEY_HOLD] [--key-press KEY_PRESS] [--play PLAY]
               [--power POWER] [--reboot] [--reset-factory] [--reset-rf-peak]
               [--rtc-get] [--rtc-set-date-dd RTC_SET_DATE_DD]
               [--rtc-set-date-mm RTC_SET_DATE_MM]
               [--rtc-set-date-yy RTC_SET_DATE_YY]
               [--rtc-set-time-hh RTC_SET_TIME_HH]
               [--rtc-set-time-mm RTC_SET_TIME_MM]
               [--rtc-set-time-ss RTC_SET_TIME_SS] [--rtc-sync]
               [--speaker SPEAKER] [--spectrum-get-band-data]
               [--spectrum-reset] [--spectrum-scan-complete]
               [--spectrum-set-band SPECTRUM_SET_BAND] [--spi-erase]
               [--spi-get] [--wait WAIT]
               port

LibGQE Command Line Interface.

optional arguments:
  --out-file OUT_FILE   Output response to specified file
  --in-file IN_FILE     Input file
  --format FORMAT       Output or input format
  --help                show this help message and exit.

interface:
  port                  RS232 interface to the unit to be controlled
  --unit UNIT           Unit model ID
  --revision REVISION   Unit firmware revision

actions available on unit::
  --echo ECHO           Set unit echo ON or OFF
  --get-battery-voltage
                        Retrieve unit battery voltage value
  --get-cfg             Retrieve unit's configuration
  --get-dsid            Undocumented command
  --get-ef              Retrieve current EF reading
  --get-emf             Retrieve current EMF reading
  --get-gyroscope       Retrieve gyroscope values
  --get-identity        Retrieve unit identity: model, firmware revision and
                        serial number
  --get-mode            Retrieve current unit operating mode
  --get-rf GET_RF       Retrieves an RF measurement
  --get-screen          Retrieve unit's LCD controller memory data
  --get-serial          Retrieve unit serial number
  --get-xyz             Retrieve magnetic field on x, y and z axes
  --key-hold KEY_HOLD   Simulate a key hold
  --key-press KEY_PRESS
                        Simulate a key press
  --play PLAY           Play a list of commands described in specified YAML
                        file
  --power POWER         Turn the unit on/off
  --reboot              Reboot the unit
  --reset-factory       Reset the unit to factory defaults
  --reset-rf-peak       Retrieve current RF reading
  --rtc-get             Retrieve unit date and time
  --rtc-set-date-dd RTC_SET_DATE_DD
                        Set RTC date day
  --rtc-set-date-mm RTC_SET_DATE_MM
                        Set RTC date month
  --rtc-set-date-yy RTC_SET_DATE_YY
                        Set RTC date year
  --rtc-set-time-hh RTC_SET_TIME_HH
                        Set RTC time hour
  --rtc-set-time-mm RTC_SET_TIME_MM
                        Set RTC time minute
  --rtc-set-time-ss RTC_SET_TIME_SS
                        Set RTC time second
  --rtc-sync            Synchronize real time clock with local computer
  --speaker SPEAKER     Set the speaker on/off
  --spectrum-get-band-data
                        Retrieve current spectrum analyzer band gain values
  --spectrum-reset      Reset spectrum band data
  --spectrum-scan-complete
                        Flagged True when the whole spectrum band has been
                        analyzed
  --spectrum-set-band SPECTRUM_SET_BAND
                        Define spectrum analyzer band ID
  --spi-erase           Erase unit's data log
  --spi-get             Retrieve unit's data log
  --wait WAIT           Wait for the specified number of seconds to elapse
```

## Disclaimer

This software is private initiative, conducted independently of [GQ Electronics LLC](http://www.gqelectronicsllc.com/comersus/store/comersus_dynamicIndex.asp?idAffiliate=7394).
