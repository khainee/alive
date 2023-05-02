pip install -U requests
echo "Running Web Server" && python -m http.server 80 &
python alive.py
