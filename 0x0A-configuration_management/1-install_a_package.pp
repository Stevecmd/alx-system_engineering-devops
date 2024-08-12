# Puppet Manifest to Install Flask from pip3
#
# This manifest ensures that Flask is installed
#  using pip3 at the specified version (2.1.0).
#
# Requirements:
# - Install Flask version 2.1.0
# - Install Werkzeug version 2.1.1

# Define the package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Define the package resource for Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
