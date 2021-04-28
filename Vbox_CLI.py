import subprocess as subprocess
import virtualbox
import shlex
import os

vbox = virtualbox.VirtualBox()
vmanager = virtualbox.Manager()
vm = [m.name for m in vbox.machines]
states = [m.state for m in vbox.machines]
################# list of VMs
print(vm)
################# States: 5=FirstOnline , 1=PoweredOff
print(states)
################# run machine
machine = vbox.machines[0]
session = vmanager.get_session()
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()
################# shutdown machine
session.console.power_down()
################# delete machine
machine = vbox.machines[2]
machine.remove("delete=true")
################# clone machine
machine.clone(snapshot_name_or_id=None,
              mode=virtualbox.library.CloneMode.machine_state,
              options=[], name="VM2",
              uuid=None, groups=[], basefolder='D:/Cloud/123', register=True)
################# change memory and cpu core
machine.lock_machine(session, virtualbox.library.LockType(2))
mute = session.machine
mute.memory_size = 2048
mute.cpu_count = 2
mute.save_settings()
session.unlock_machine()

################# run a command on VM
path = 'C:\Program Files\Oracle\VirtualBox'
os.chdir(path)
command = shlex.split("VBoxManage help guestcontrol")
command1 = shlex.split("VBoxManage guestcontrol") + [machine.name] + shlex.split(
    " --username sajjad --password sajjad run  --exe /bin/ls ")
shutdown = shlex.split("VBoxManage controlvm") + [machine.name] + ["poweroff"]
# start = shlex.split("VBoxManage startvm") + [machine.name]
process = subprocess.Popen(command1,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout = str(stdout).encode("utf-8")
print(stdout.decode("unicode_escape"))
stderr = str(stderr).encode("utf-8")
print(stderr.decode("unicode_escape"))
print(states)
