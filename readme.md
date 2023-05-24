# W.I.C - Web Image Converter

Wic is very simple python program that converts png, jpg and jpeg images to webp format.
WIC is a command-line program that is distributed for windows via exe file.

## Installation

_Windows is probably very scared about this executable and you might get warnings_

1. Download executable
2. (optional but strongly recommended) add WIC to PATH and it can be launched from any directory by typing wic to explorer address bar.

## Commands

Wic searches image files from the directory where IT IS LAUNCHED. That is why it should be added to PATH. Using wic is relatively easy. WIC supports following commands:

- help - Print commands
- convert - Converts all found images in working directory to webp format
- list - List all images with file path in working directory.
- count - Display image count in working directory.
- countout - Display converted image count in output directory.
- license - Show licence
- exit - Exit program

### Converting

_Be carefull with '00_img_out' folder that WIC creates, directory content gets rebuild every time WIC is given command 'convert' and confirmation is answered with 'y' or 'Y'._

Assuming WIC is added to PATH.

1. Browse to folder where image files are located.
2. Type 'wic' to address bar and WIC should open.
3. Write convert command.
4. Give quality percentage for wic when it asks
5. WIC converts images and outputs them to subfolder
6. Type exit to close WIC

Without adding WIC to PATH. (Not recommended).

1. Move images to same folder where wic.exe is.
2. Double click wic.exe
3. Write convert command.
4. Give quality percentage for wic when it asks
5. WIC converts images and outputs them to subfolder
6. Type exit to close WIC
