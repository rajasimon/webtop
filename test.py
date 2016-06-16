import time
import subprocess
import tempfile

f = tempfile.TemporaryFile()
p = subprocess.Popen(['top'], stdout=f)
time.sleep(2)
p.terminate()
p.wait()
f.seek(0)
print(f.read().decode())
f.close()
