__author__ = 'mccoydo'
import psutil, os

procname = 'iexplorer.exe'

# try:
#     for proc in psutil.process_iter():
#         if procname in proc.name():
#             p = psutil.Process(proc.pid)
#
#             if not 'SYSTEM' in p.username:
#                 proc.kill()
# except psutil.AccessDenied:
#     pass
os.system('taskkill /f /IM chrome.exe')
