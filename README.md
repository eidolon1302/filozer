# File Organizer CLI

A command-line tool to organize and clean files in your directories.

## Features

- **Organize**: Moves files into categorized subfolders (e.g., Images, Documents, Audio).
- **Clean**: Deletes old files based on their last modified date.

## Installation

To install this CLI tool, you can use pip directly from the GitHub repository:

```bash
pip install git+https://github.com/eidolon1302/cli-mad.git
```

## Usage

### Organize Files

To organize files in the current directory:

```bash
file-organizer organize
```

To organize files in a specific directory (e.g., your Downloads folder):

```bash
file-organizer organize C:\Users\YourUser\Downloads
```

### Clean Files

To clean files older than 30 days in the current directory (default):

```bash
file-organizer clean
```

To clean files older than 90 days in a specific directory:

```bash
file-organizer clean C:\Users\YourUser\Documents --days-old 90
```

To perform a dry run (simulate cleaning without actually deleting files):

```bash
file-organizer clean --dry-run
```

## Development

If you want to develop this tool, you can install it in editable mode:

```bash
pip install -e .
```

Then, you can run it using `python -m file_organizer <command> <args>`.

## Contributing

Feel free to contribute by opening issues or pull requests on the [GitHub repository](https://github.com/eidolon1302/cli-mad).