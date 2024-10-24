# Basic usage (generates 10 entries with 1 second delay)
python3 generate_logs.py

# Generate logs continuously with 0.5 second delay
python3 generate_logs.py --continuous --delay 0.5

# Generate 100 entries quickly (0.1 second delay)
python3 generate_logs.py --entries 100 --delay 0.1

# Use custom log file locations
python3 generate_logs.py --access-log ./access.log --error-log ./error.log
