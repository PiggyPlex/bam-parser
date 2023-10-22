import winreg
import struct

BAM_PATH = r'SYSTEM\CurrentControlSet\Services\bam\State\UserSettings'
bam_output = []

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, BAM_PATH) as key:
  for i in range(winreg.QueryInfoKey(key)[0]):
    sid = winreg.EnumKey(key, i)
    with winreg.OpenKey(key, sid) as sid_key:
      for j in range(winreg.QueryInfoKey(sid_key)[1]):
        name, value, _ = winreg.EnumValue(sid_key, j)
        if name == 'SequenceNumber' or name == 'Version':
          continue
        date = struct.unpack("<Q", value[0:8])[0]
        bam_output.append((name, date, sid))

print(bam_output)
