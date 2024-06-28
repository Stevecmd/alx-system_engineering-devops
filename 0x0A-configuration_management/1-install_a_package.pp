# Puppet Manifest to Install Flask from pip3
#
# This manifest ensures that the Flask package is installed
#  using pip3 at the specified version (2.1.0).
#
# Requirements:
# - Install Flask
# - Flask version must be 2.1.0
#
# Usage:
# 1. Save this file as 1-install_a_package.pp
# 2. Run `puppet-lint 1-install_a_package.pp` to check for syntax issues.
# 3. Apply the manifest with `puppet apply 1-install_a_package.pp`.
# 4. Verify the installation with `flask --version`.

# Define the package resource
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
