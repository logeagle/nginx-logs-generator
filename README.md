Here's a script to install all the necessary dependencies for all three components (log processor, dashboard, and log generator) that we created:

```bash
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

```

Alternatively, you can create a requirements.txt:

```text
# Core dependencies
pandas>=1.5.0
pyarrow>=12.0.1
watchdog>=3.0.0

# Dashboard dependencies
dash>=2.9.0
flask-caching>=2.0.0
plotly>=5.13.0
waitress>=2.1.2

```

You can install using either method:

Method 1 - Using the bash script:
```bash
# Save the first script as install.sh
chmod +x install.sh
./install.sh
```

Method 2 - Using requirements.txt:
```bash
# Save the second file as requirements.txt
pip3 install -r requirements.txt
```

For both methods, you might need to use sudo if installing globally:
```bash
sudo pip3 install -r requirements.txt
```

Extra notes:
1. If you get any permission errors, you can add the `--user` flag:
```bash
pip3 install --user -r requirements.txt
```

2. If you're using a virtual environment (recommended):
```bash
python3 -m venv logeagle-env
source logeagle-env/bin/activate
pip3 install -r requirements.txt
```

3. If you need to upgrade pip first:
```bash
pip3 install --upgrade pip
```

After installation, verify everything works:
```bash
python3 -c "import pandas, pyarrow, watchdog, dash, flask_caching, plotly"
```

If you don't see any errors, the installation was successful!