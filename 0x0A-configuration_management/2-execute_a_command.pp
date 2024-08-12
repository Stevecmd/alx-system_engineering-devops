# Puppet Manifest to Kill a Process Named 'killmenow'
#
# This manifest utilizes the `exec` resource in Puppet to
# terminate a process named 'killmenow' using `pkill`.
# The `pkill` command sends a signal to all processes with
# the specified name, effectively terminating them.
#
# Requirements:
# - Use the `exec` Puppet resource
# - Use `pkill` to terminate the process
#
# Example Usage:
# 1. Start the process `killmenow` in one terminal.
# 2. Apply the manifest with `puppet apply 2-execute_a_command.pp`.
# 3. Verify that the process is terminated.

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => shell,
}
