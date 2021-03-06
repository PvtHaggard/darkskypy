Pydarksky!
==========
[![Build Status](https://travis-ci.org/PvtHaggard/pydarksky.svg?branch=master)](https://travis-ci.org/PvtHaggard/pydarksky) [![License](https://img.shields.io/badge/License-GNU%20v3.0-blue.svg)](https://github.com/PvtHaggard/pydarksky/blob/master/LICENSE) ![Python](https://img.shields.io/badge/Python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.6-blue.svg) ![Status](https://img.shields.io/badge/Status-Release-green.svg)



Pydarksky is a work in progress wrapper for the [Dark Sky](https://www.darksky.net) API.

-----

This is the first python library I have written so any advice and help will be greatly appreciated.

### TODO:
* Documentation
    * Docstrings
    * Code comments
    * Readme
* Rewrite unittests
* Example uses


----
### Install
Python versions 2.7, 3.3+
```
pip install pydarksky
```

### Basic usage
Example uses [pendulum](https://github.com/sdispater/pendulum) for timestamp conversion.
```python
import pendulum
import pydarksky

pendulum.set_formatter("alternative")

weather = pydarksky.weather(api_key=API_KEY, latitude=-34.9285, longitude=138.6005)

# Current weather
if weather.has_now():
    print("Now:")
    date = pendulum.from_timestamp(weather.now.time, tz=weather.timezone)
    try:
        temperature = weather.now.temperature
    except pydarksky.NoDataError:
        temperature = "No Data"

    print("Time: {}, Temp: {}\n".format(date.format("DD-MM-YY hh:mm"), temperature))


# Iterating over forecast
if weather.has_daily():
    print("Daily:")
    for day in weather.daily:
        date = pendulum.from_timestamp(day.time, tz=weather.timezone)
        try:
            temperature = day.temperatureHigh
        except pydarksky.NoDataError:
            temperature = "No Data"

        print("Time: {}, Temp: {}".format(date.format("DD-MM-YY"), temperature))
```

### Weather request
```python
# DarkSky instantiation
>>> darksky = pydarksky.DarkSky(API_KEY)

# Pre-define values
>>> darksky.latitude = -34.9285
>>> darksky.longitude = 138.6005
>>> weather = darksky.weather()

# Pass values as params
>>> weather = darksky.weather(latitude=-34.9285, longitude=138.6005)

# Pass values from dict
>>> kwargs = {"longitude": 138.6005, "latitude": -34.9285}
>>> weather = darksky.weather(**kwargs)
```

### Historical Request
Unlike the longitude/latitude the date must be passed every time a historical request is wanted.
Darksky.net will use the locations timezone by default so specifying it yourself is not required.

```python
>>> import pydarksky
>>> from datetime import datetime
>>> darksky = pydarksky.DarkSky(API_KEY)

>>> darksky.weather(latitude=-34.9285, longitude=138.6005, date=datetime(2017, 1, 1))
```

### Setting data blocks to exclude from response
You can opt to exclude specific data blocks from the API response by setting the `DarkSky.exclude` attribute to one or more of the valid values found in `DarkSky.EXCLUDES`. Excluding data blocks can be used to reduce server response latency.

`DarkSky.exclude_invert()` can be used to invert the values in `DarkSky.exclude`. This is useful if you know which data blocks you need but not the ones you don't.

```python
>>> import pydarksky
>>> darksky = pydarksky.DarkSky(API_KEY)

>>> darksky.EXCLUDES
('currently', 'minutely', 'hourly', 'daily', 'alerts', 'flags')

>>> darksky.exclude = ["alerts", "flags"]
>>> darksky.exclude
['alerts', 'flags']

>>> darksky.exclude = "alerts"
>>> darksky.exclude
['alerts']

>>> darksky.exclude = ["abc"]
ValueError: 'abc' is not a valid exclude value

>>> darksky.exclude_invert()
>>> darksky.exclude
['currently', 'minutely', 'hourly', 'daily']
```

### Setting number of hourly data blocks received
You can increase the hour-by-hour data returned from 48, to 168 by setting the `DarkSky.extend` attribute to `True`. The default value is `False`.

### Setting response language
```python
>>> import pydarksky
>>> darksky = pydarksky.DarkSky(API_KEY)

>>> darksky.LANGS
['Arabic', 'Azerbaijani', 'Belarusian', 'Bosnian', 'Bulgarian', ...]

>>> darksky.lang
'auto'

>>> darksky.lang = 'English'
>>> darksky.lang
'en'

>>> darksky.lang = 'it'  # 'it' == 'Italian'
>>> darksky.lang
'it'

>>> darksky.lang = "abc"
ValueError: 'abc' is not a valid response language
```


### Setting response units

Valid units values:

* **auto**: automatically select units based on geographic location
* **ca**: same as si, except that windSpeed is in kilometers per hour
* **uk2**: same as si, except that nearestStormDistance and visibility are in miles and windSpeed is in miles per hour
* **us**: Imperial units (the default)
* **si**: SI units


```python
>>> import pydarksky
>>> darksky = pydarksky.DarkSky(API_KEY)

>>> darksky.UNITS
('auto', 'ca', 'uk2', 'ui', 'si')

>>> darksky.units
'auto'

>>> darksky.units = "si"
>>> darksky.units
'si'

>>> darksky.units = "abc"
ValueError: 'abc' is not a valid unit type
```



<a href="https://darksky.net/poweredby/"> <img src="https://darksky.net/dev/img/attribution/poweredby-oneline.png" alt="Dark Sky" width="500px"/></a>
