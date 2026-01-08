## License Notice

This project is a modified and repackaged version of **lpunpack**,
originally developed by **unix3dgforce** and licensed under the
**GNU Lesser General Public License v3.0 (LGPL-3.0)**.

Original source repository:
https://github.com/unix3dgforce/lpunpack

The library portion of this project remains licensed under LGPL-3.0.
The corresponding source code for the modified library is provided in
this repository to comply with the terms of the LGPL.

Prebuilt binary releases (Windows `.exe`) are provided for convenience
only. You are free to rebuild the binaries yourself using the provided
source code and build scripts.

# lpunpack

**lpunpack.exe** / **lpunpack_cli.py** — command-line tool for extracting Android
partition images from `super.img`.

## Usage

### Binary (Recommended – No Python Required)

    lpunpack.exe [options] SUPER_IMAGE OUTPUT_DIR

### Python (From Source)

    python lpunpack_cli.py [options] SUPER_IMAGE OUTPUT_DIR

## Positional Arguments

    SUPER_IMAGE
        Path to the Android super image

    OUTPUT_DIR
        Directory to extract partition images into

## Optional Arguments

    -h, --help
        Show this help message and exit

    -p NAME, --partition NAME
        Extract the specified partition.
        Can be specified multiple times or separated using "," or ":"

    -S NUM, --slot NUM
        Slot number (default is 0)
        NOTE: Slot A/B index extraction is not implemented yet.

    --info
        Display partition metadata without extracting images

    --no-info
        Disable metadata display

    -f {text,json}, --format {text,json}
        Select output format for --info (default: text)

## Notes

- Slot A/B index extraction is NOT implemented.
- Behavior and output format are consistent with the original lpunpack tool.
- Binary releases are provided for convenience; rebuilding from source is supported.

