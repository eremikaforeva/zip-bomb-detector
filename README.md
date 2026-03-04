# Zip Bomb Detector 🔍

A Python-based security tool that detects potential **ZIP bomb attacks** using static archive analysis.

## What is a Zip Bomb?

A zip bomb is a malicious compressed file designed to crash systems by expanding into extremely large amounts of data when extracted.

Example:
- 42KB zip file
- expands to **gigabytes or petabytes**

This tool analyzes archives **without extracting them**, making detection safe.

## Features

✔ Compression ratio analysis  
✔ Nested ZIP detection  
✔ CLI arguments (`--ratio`, `--deep`)  
✔ JSON output for automation  

## Usage

Basic scan:

```bash
python3 zip_detector.py file.zip

