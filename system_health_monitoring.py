'''
1. System Health Monitoring Script:
Develop a script that monitors the health of a Linux system. It should check
CPU usage, memory usage, disk space, and running processes. If any of
these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the
script should send an alert to the console or a log file.
'''

''' Script owner -> Deepa Shelar [deepashelar7@gmail.com] '''


import psutil
import logging
import time
from datetime import datetime

logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
PROCESS_THRESHOLD = 200  # total number of processes

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {usage}%')
    return usage

def check_disk_space():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {usage}% used')
    return usage

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f'High number of running processes detected: {process_count}')
    return process_count

def main():
    logging.info('System Health Monitoring Script Started')

    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_space()
        running_processes = check_running_processes()

        logging.info(f'CPU Usage: {cpu_usage}%')
        logging.info(f'Memory Usage: {memory_usage}%')
        logging.info(f'Disk Usage: {disk_usage}%')
        logging.info(f'Running Processes: {running_processes}')

        time.sleep(60)

if __name__ == '__main__':
    main()
