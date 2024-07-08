# Puppet script to configure a new Ubuntu server with Nginx and a custom HTTP header

# Update the system's package list
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'], # Depends on system update
}

# Create a simple index.html file in the web root
file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!', # Content of the index.html file
}

# Configure Nginx to use a custom site configuration
# This configuration should include the custom HTTP header and any necessary redirects
file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'), # Use a template for Nginx configuration
  require => Package['nginx'], # Depends on Nginx package installation
  notify  => Service['nginx'], # Notify Nginx service to reload on file change
}

# Ensure the Nginx service is running and enabled to start on boot
service {'nginx':
  ensure  => running,
  require => File['/etc/nginx/sites-available/default'], # Depends on the Nginx site configuration
}
