# Install and configure Nginx to meet specific requirements

# Ensure the system is updated
exec { 'update system':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin'],
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

# Create the index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['nginx'],
}

# Directly configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @(EOF)
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 http://example.com;
    }
}
  | EOF
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
