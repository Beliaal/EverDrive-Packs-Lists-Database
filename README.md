# Hardware Target Game Database

The Hardware Target Game Database is an archival research initiative
with the goal of allowing users to build real-hardware optimized ROM
packs based on suggested file/folder layouts.

Because most flash-carts and optical drive emulators require specific
ROMs and fixes, it is a monumental task to compile 100%
complete/working setups, and is often beyond the capabilities of any
one person. Thousands of hours have been invested in the
*SourceMaterial DataBases* (or SMDBs) of this project with the goal of
100% complete, 100% working real-hardware compatible arrangements of
the highest quality ROM dumps. File hierarchies are shared via SMDB
text files which contain all of the information needed to identify,
sort and rename files.

What's in a SMDB file? A SMDB file generated by the `parse_pack`
script is a simple archival text record describing exact files (using
hash values) and the location of these files withing a folder
hierarchy. One record per line, six tab-separated columns per record:

1. [SHA256](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) value,
2. folder and file name (Unix/Linux format),
3. SHA1,
4. MD5,
5. CRC32,
6. file size (in bytes, **new feature not yet available in all SMDBs**)

SMDBs are provided for a range of flash-carts.  These SMDBs allow
users to dump all of their legally acquired ROMs into a single folder
(zip files accepted). When the `build_pack` script is run on that
directory, the ROMs will be analyzed (via hash comparisons), renamed
and sorted into complete, flash-cart friendly Packs, as described in
an SMDB.  This allows creators to share file and folder setups without
having to share the ROMs themselves.

## Tools Included

The `build_pack`, `parse_pack` and `verify_pack` scripts are written in python3. To launch
a script, install [python](https://www.python.org) if need be, and then open
a Windows console or a Linux/Unix terminal.

**parse_pack.py** For making SMDBs (example command):
```DOS .bat
"C:\XXX\parse_pack.py" -f "C:\XXX\Folder to be parsed" -o "C:\XXX\SMDB.txt"
```

`-f` (or `--folder`) indicates the target ROM pack

`-o` (or `--output`) is the text file that will contain the hash
values, filenames, and folder structure


**build_pack.py** For building a pack based on a pre-made SMDB (example command):
```DOS .bat
"C:\XXX\build_pack.py" -i "C:\XXX\Folder with unorganized ROMs" -d "C:\XXX\SMDB.txt" -o "C:\XXX\Output folder for rebuilt pack" -m "C:\XXX\Missing.txt"
```

`-i` (or `--input_folder`) is the folder containing the unorganized
ROMs

`-d` (or `--database`) is the SMDB file describing the way your ROMs
are organized

`-o` (or `--output_folder`) is the folder in which to build the ROM
pack

`-m` (or `--missing`) is the text file that will list the ROMs missing
in order to reach the 100% mark

Options for advanced users:

`--file_strategy {copy,hardlink,smart}` changes the way files are
copied to the destination folder. The default is to physically
duplicate the files (`copy`). The options `hardlink` and `smart` avoid
file duplication and saves storage space for pack builders, only on
filesystems supporting this feature. Use `hardlink` when both source
and destination files are on the same filesystem, and `smart` when
destination files are on another filesystem. Please note that when
copying to a FAT32 or exFAT SD card, hardlinks are automatically
converted into normal files.

`-s` (or `--skip_existing`) avoids overwriting files that already
exist in the destination folder.

`-x` (or `--drop_initial_directory`) skips the first directory level
of the SMDB pack, so you can rename it to your convenience. For
instance, if your output folder is `./NES/`, the pack will be built
under `./NES/EverDrive N8/...`. With the option
`--drop_initial_directory`, the pack will be built directly under
`./NES/...`.


**verify_pack.py** For verifying pack folders match up correctly with SMDBs (example command):
```DOS .bat
"C:\XXX\verify_pack.py" -f "C:\XXX\Folder to be parsed" -d "C:\XXX\SMDB.txt" -m "C:\XXX\Mismatch.txt"
```

`-f` (or `--folder`) indicates the target ROM pack

`-d` (or `--database`) is the SMDB file describing the way your ROMs
are organized

`-m` (or `--mismatch`) is the text file that will list the ROMs in incorrect locations,
extra files, and ROMs missing when compared to the SMDB.

`-x` (or `--drop_initial_directory`) skips the first directory level
of the SMDB pack, so you can rename it to your convenience. For
instance, if your pack folder is `./NES/`, the pack will be verified
using `./NES/EverDrive N8/...`. With the option
`--drop_initial_directory`, the pack will be verified using `./NES/...`.


Depending on your python installation, you may need to begin your
command with the location of `python.exe` (for example,
`C:\Users\XXX\AppData\Local\Programs\Python\Python36-32\python.exe`). More
information for pack builders are available in the
[wiki](https://github.com/SmokeMonsterPacks/EverDrive-Packs-Lists-Database/wiki).

## GUI

A graphical user interface is available in
[@Aleyr](https://github.com/Aleyr)'s
[repository](https://github.com/Aleyr/EverDrive-Packs-Lists-Database-UI) for
both the `build_pack.py` and `parse_pack.py` scripts. If you are
having difficulty with the command line options, please consider
trying the GUI version.

## Requirements

[python](https://www.python.org) 3.5 or newer

Linux, MacOS, or Windows

## Coding

Scripts and code by
[@frederic-mahe](https://github.com/frederic-mahe) and
[@steve1515](https://github.com/steve1515), with awesome
patches by [@eatnumber1](https://github.com/eatnumber1),
[@coughlanio](https://github.com/coughlanio)
and [@Slashbunny](https://github.com/Slashbunny).

EverDrive Pack SMDB layouts by
[@SmokeMonsterPacks](https://github.com/SmokeMonsterPacks).

[GUI](https://github.com/Aleyr/EverDrive-Packs-Lists-Database-UI) by [@Aleyr](https://github.com/Aleyr).

## Similar tools

- [GammaCopy](https://github.com/fartwhif/GammaCopy) (Windows only, direct support of SMDB files, fast execution)
- [clrmamepro](https://mamedev.emulab.it/clrmamepro/),
- [romcenter](http://www.romcenter.com/),
- [romvault](http://www.romvault.com/),
- [SabreTools](https://github.com/SabreTools/SabreTools)
