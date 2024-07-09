# Puppet script to configure a new Ubuntu server with Nginx and a custom HTTP header

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure the necessary directories exist
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Create index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Create 404.html
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Configure Nginx directly in the manifest
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOF"),
server {
    listen      80;
    listen      [::]:80;
    add_header  X-Served-By $hostname;
    root        /var/www/html;
    index       index.html index.htm;

    location /redirect_me {
        return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}
| EOF
  notify  => Service['nginx'],
  mode    => '0644',
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
