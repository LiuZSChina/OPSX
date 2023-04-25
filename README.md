# OPSX Sonnar
An open sourced Polaroid SX-70 core board with sonnar support.Based on the [OPSX project](https://github.com/sunyitong/OPSX).\
开源的宝丽来sx-70核心板，可以支持带有声呐对焦的设备。基于[OPSX 项目](https://github.com/sunyitong/OPSX)开发。

This is an open sourced Polaroid SX-70 instant camera core board with the Raspberry Pi RP2040 as the MCU. The aim of this project is to provide a fully resource accessible and hobbyist friendly replacement core board. It offers more extensibility and hacking ideas while implementing all the features of the original camera.\
本项目是开源的宝丽来sx-70核心板，该项目使用树莓派rp2040构建而成，本项目的目的是为爱好者提供一个可以完全自主掌控的核心板，在保留原机器各种功能的同时可以发挥自己的创意进行功能拓展。

The structure of the repository:\
本项目仓库的结构：

1. The [bom](https://github.com/sunyitong/OPSX/tree/master/bom) folder contains an html-based interactive bill of material. You can use it to find the component types and locations

2. The [code](https://github.com/sunyitong/OPSX/tree/master/code) folder holds the program files necessary to run the core board. The programs are implemented in two separate programming languages:

   - [Micropython](https://docs.micropython.org/en/latest/rp2/quickref.html): Similar syntax to python, easy to modify and testing.
   - [Rust](https://docs.rs/rp2040/latest/rp2040/) (TODO): Ultimate performance with zero runtime loss.

3. The [gerber](https://github.com/sunyitong/OPSX/tree/master/gerber) folder stores the PCB files necessary for factory production.

4. The [schematic](https://github.com/sunyitong/OPSX/tree/master/schematic) folder holds a PDF file which illustrating the circuit principles.

5. The [NewPCB](https://github.com/LiuZSChina/OPSX/tree/master/NewPCB) contains almost every thing related to sonnar model.\
与声呐型号有关的所有文件（PCB工程，代码文件）都在[NewPCB文件夹](https://github.com/LiuZSChina/OPSX/tree/master/NewPCB) 内.

## Table of Contents

- [OPSX](#opsx)
  - [Table of Contents](#table-of-contents)
  - [Hardware](#hardware)
    - [Fabrication](#fabrication)
  - [Software](#software)
    - [Uploading](#uploading)
  - [Contributor](#contributor)
  - [License](#license)


## Hardware
TODO
> Remander: Special tools are required to replace the original core board, please read the [Disassembly Guide](https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf) first.
### Fabrication
Please select a **dual copper layer PCB** with a thickness of **0.8 mm** or less for fabrication.
## Software
TODO
### Uploading
TODO
## Contributor
[@Yitong Sun](https://github.com/sunyitong) - a PhD candidate in the Computer Science Research Centre at the Royal College of Art.

[RCA website](https://www.rca.ac.uk/research-innovation/research-degrees/research-students/yitong-sun/) - [E-mail](yitong.sun@network.rca.ac.uk)
## License
Any distribution or modification based on this project should be clearly attributed to the source.
[GPL 3.0](LICENSE) © Yitong Sun