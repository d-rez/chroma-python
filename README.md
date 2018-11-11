# ChromaPython Turbo

## Update by d-rez
The original repository uses PUT without the KeepAlive header (so new connecton on every request), parses JSON response after receiving it and then decodes it. This is fine in "casual" use but horrible when used for apps like visualisers.

This fork uses a different approach - we don't care about the response (assume it's fine) and set the timeout to something extra small. On top of that we make use of Connection:KeepAlive header by using requests.Session. This improves the performance **DRASTICALLY**. I'm serious. Check out the video

>>>TODO video lol, soon

[![Build status](https://ci.appveyor.com/api/projects/status/5ihmbuppv3g29or2/branch/master?svg=true)](https://ci.appveyor.com/project/Vaypron/chroma-python-ee89l/branch/master)

## Disclaimer
This project is still in active development!

## Support

### Devices
```
Keyboard
Headset
Mouse
Headset
Keypad
ChromaLink
```

### BCA
#### Read
```
Keyboard
```
#### Write
```
.
```

## How to install

### Auto-Install with pip

```
Coming soon.
```

### Install with pip (currently recommended)

1. Clone the repository
2. Navigate into the directory and run:
```
pip install .
```

Pip should now install all necessary dependencies, as well as ChromaPython itself.

### By using the Source files:

Requirements:
```
requests
```
Can be installed by
```
pip install requests
```

After installing requests, clone the repository and copy all files of the ChromaPython folder into your working directory.


## Contributing
Feel free to contribute by reporting issues and/or extending the current code. You can do this by forking this project
and creating a pull request. Unfinished tasks can be found as "enhancement" issues.
Also, please always add comments to your changes/new code.

## How to use

Take a look at ```Tests\checkall.py```. It should give you a good example on how to use it.
An example on how to use the BCA feature can be found in```Test\checkBinary.py```.
