#!/bin/bash

echo "Installing Python dependencies for Log Eagle system..."

# Create and activate virtual environment (optional but recommended)
echo "Creating virtual environment..."
python3 -m venv logeagle-env
source logeagle-env/bin/activate

# Install dependencies for log processor
echo -e "\nInstalling log processor dependencies..."
pip3 install pyarrow \
            pandas \
            watchdog

# Install dependencies for dashboard
echo -e "\nInstalling dashboard dependencies..."
pip3 install dash \
            flask-caching \
            plotly \
            waitress

# No additional dependencies needed for log generator
echo -e "\nInstallation complete!\n"

# Show installed packages and versions
echo "Installed packages:"
pip3 freeze

echo -e "\nYou can now run:"
echo "1. Log processor: ./log_processor.py"
echo "2. Dashboard: ./log_dashboard.py"
echo "3. Log generator: sudo ./generate_logs.py"