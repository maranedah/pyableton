# Ableton Parser Library for Python


![Python version](https://img.shields.io/badge/python-3.10-blue)

A Python library for parsing and working with Ableton Live files (.als). This library provides functionality to extract information from Ableton Live projects, making it easier to analyze, manipulate, and interact with Ableton Live sets programmatically.

## Features

- **Parse Ableton Live Files:** Extract information from Ableton Live project files (.als).
- **Retrieve Track and Clip Data:** Access track information, clip details, and other relevant data.
- **Flexible and Extensible:** Designed for ease of use and extensibility for custom use cases.

## Installation

```bash
pip install pyableton
```

## Usage

```python
from pyableton import Ableton

# Initialize the parser with the path to your Ableton Live file
ableton_data = Ableton("path/to/your/project.als")

# Get midi information
midi_data = ableton_data.to_muspy()
```

For detailed usage instructions and API documentation, please refer to the documentation (WIP).

## Contributing

We welcome contributions! If you find a bug, have a feature request, or would like to contribute code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
