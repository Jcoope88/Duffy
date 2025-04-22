init:
	python3 -m venv venv
activate:
	source /home/jcooper/scratch/SystemMonitor/venv/bin/activate && pip3 install -r requirements.txt
run:
	python3 -m main.py
