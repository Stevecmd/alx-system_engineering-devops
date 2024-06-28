# Puppet Manifest to Install Flask from pip3
#
# This manifest ensures that Flask is installed
#  using pip3 at the specified version (2.1.0).
#
# Requirements:
# - Install Flask
# - Flask version must be 2.1.0

# Define the package resource
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
