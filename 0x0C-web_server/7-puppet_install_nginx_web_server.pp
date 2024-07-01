# Install and configure an Nginx server using Puppet

# Ensure the system is updated
exec { 'update system':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin'],
  unless  => 'test -f /var/lib/apt/periodic/update-success-stamp',
}

# Install Nginx package
package { 'nginx':
  ensure   => installed,
  require  => Exec['update system'],
}

# Ensure the firewall allows HTTP traffic
exec { 'allow nginx http':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  path    => ['/usr/sbin', '/usr/bin', '/bin'],
  unless  => '/usr/sbin/ufw status | grep -q "Nginx HTTP.*ALLOW IN"',
  require => Package['nginx'],
}

# Create a custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['nginx'],
}

# Create the index.html file with the required content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['nginx'],
}

# Configure Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => File['/etc/nginx/sites-available/default'],
}

# Custom template for Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @(EOF)
/**
 * Nginx default server configuration file
 */
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
  | EOF
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
}
