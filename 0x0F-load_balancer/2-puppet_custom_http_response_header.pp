# Puppet script to configure a new Ubuntu server with Nginx, a custom HTTP header, and system update

# Update system package list
exec { 'update system':
  command => '/usr/bin/apt-get update',
  path    => ['/bin/', '/usr/bin/'],
}

# Install nginx package with system update requirement
package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
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

# Add redirect rule using exec resource
exec { 'redirect_me':
  command     => 'sed -i "24i\\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  path        => ['/bin/', '/usr/bin/'],
  refreshonly => true,
  subscribe   => Package['nginx'],
}

# Add custom HTTP header using exec resource
exec { 'HTTP header':
  command     => 'sed -i "25i\\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  path        => ['/bin/', '/usr/bin/'],
  refreshonly => true,
  subscribe   => Package['nginx'],
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => [Exec['redirect_me'], Exec['HTTP header']],
}
