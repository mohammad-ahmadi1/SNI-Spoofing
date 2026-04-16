# SNI-Spoofing

A small Python project for SNI spoofing and DPI bypass experiments using TCP/TLS packet manipulation.

## Features
- Local TCP listener
- Fake TLS ClientHello injection with configurable SNI
- Packet interception using WinDivert (`pydivert`)
- Configurable target IP/port and listen address

## Requirements
- Python 3.10+
- Windows (required for WinDivert/`pydivert`)
- Administrator privileges (needed for packet interception)

## Quick Setup
Run the setup script:

```bash
python setup_env.py
```

This script creates a virtual environment and installs dependencies from `requirements.txt`.

## Configuration
Edit `config.json`:

```json
{
  "LISTEN_HOST": "0.0.0.0",
  "LISTEN_PORT": 40443,
  "CONNECT_IP": "188.114.98.0",
  "CONNECT_PORT": 443,
  "FAKE_SNI": "auth.vercel.com"
}
```

## Run
After setup:

```bash
python main.py
```

## Notes
- This project is for research and educational use.
- Use only in environments where you have permission.
