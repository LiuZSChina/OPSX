# OPSX Sonnar
An open sourced Polaroid SX-70 core board with sonnar support.Based on the [OPSX project](https://github.com/sunyitong/OPSX).\
开源的宝丽来sx-70核心板，可以支持带有声呐对焦的设备。基于[OPSX 项目](https://github.com/sunyitong/OPSX)开发。

This is an open sourced Polaroid SX-70 instant camera core board with the Raspberry Pi RP2040 as the MCU. The aim of this project is to provide a fully resource accessible and hobbyist friendly replacement core board. It offers more extensibility and hacking ideas while implementing all the features of the original camera.\
本项目是开源的宝丽来sx-70核心板，该项目使用树莓派rp2040构建而成，本项目的目的是为爱好者提供一个可以完全自主掌控的核心板，在保留原机器各种功能的同时可以发挥自己的创意进行功能拓展。

The structure of the repository:\
本项目仓库的结构：

1. The [Original](https://github.com/LiuZSChina/OPSX/tree/master/Original) file contains design for non-sonnar sx-70.See README.md inside this folder for details.\
[Original](https://github.com/LiuZSChina/OPSX/tree/master/Original)文件夹内是适合没有声呐对焦sx70的核心板设计，设计来自于原本的[OPSX 项目](https://github.com/sunyitong/OPSX)，文件夹内具体项目的作用详见文件夹内的README.md

2. The [Sonar](https://github.com/LiuZSChina/OPSX/tree/master/Sonnar) file contains design for sonnar sx-70.See README.md inside this folder for details.\
[Original](https://github.com/LiuZSChina/OPSX/tree/master/Original)文件夹内是新设计的适用于声呐对焦的sx70核心板及附件，文件夹内具体项目的作用详见文件夹内的README.md。



## Table of Contents

- [OPSX](#opsx)
  - [Hardware](#hardware)
    - [Fabrication](#fabrication)
  - [Software](#software)
    - [Uploading](#uploading)
  - [Contributor](#contributor)
  - [License](#license)


## Hardware
> Remander: You are going to need some “basic” tools:   soldering iron with a fine tip, a prying tool and a tweezer.\
Aside from the usual tools you are going to need what is called a “Polaroid screwdriver” or “SX-70 screwdriver”, since most of the cameras use a special “square 1mm x 1mm” screws. You could either buy one or fabricate one yourself.\
please read the [Disassembly Guide](https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf) or [SX70 camera 125ASA to 600ASA conversion](https://opensx70.com/tutorials/100-600-conversion/) first.\
提示：首先你需要一些基本的工具：电烙铁、撬棒和镊子。\
其次大多数sx70相机的螺丝都是非常特殊的1mm x 1mm 宝丽来螺丝，所以你需要使用特殊的螺丝刀才能拆卸，买一把或者自己磨一个都可以。\
在操作之前推荐先浏览[Disassembly Guide](https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf) 或者 [SX70 camera 125ASA to 600ASA conversion](https://opensx70.com/tutorials/100-600-conversion/).

### Fabrication
Please select a **dual copper layer PCB** with a thickness of **0.8 mm** or less for fabrication.\
制造时请选择 FR-4基板，双层板，厚度0.8mm或者更小（会贵）。

## Software
TODO

### Uploading
Solder U+ U- GND VCC to a standard usb cable to connect to your computer. Then you can treat it as normal raspberry pico device. See [here](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#raspberry-pi-pico) for more information about uploading.\
把板子上的U+ U- GND VCC焊到usb线上，连接电脑后可以当作树莓派Pico开发板进行操作，具体上传的方法在[这里](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#raspberry-pi-pico)。

## Contributor
[@Yitong Sun](https://github.com/sunyitong) - a PhD candidate in the Computer Science Research Centre at the Royal College of Art.[RCA website](https://www.rca.ac.uk/research-innovation/research-degrees/research-students/yitong-sun/) - [E-mail](yitong.sun@network.rca.ac.uk)

[@LiuZS](https://github.com/LiuZSChina) - ？
## License
Any distribution or modification based on this project should be clearly attributed to the source.
[GPL 3.0](LICENSE)