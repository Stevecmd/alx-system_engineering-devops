# Puppet Manifest to Create a File in /tmp
#
# This manifest ensures that a file named 'school' is created in the /tmp directory
# with specific ownership, permissions, and content as specified in the requirements.
#
# Usage:
# 1. Save this file as 0-create_a_file.pp
# 2. Run `puppet-lint 0-create_a_file.pp` to check for syntax issues.
# 3. Apply the manifest with `puppet apply 0-create_a_file.pp`.
# 4. Verify the file creation with `ls -l /tmp/school` and `cat /tmp/school`.

# Define the file resource
file { '/tmp/school':
ensure  => present,
content =>'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
