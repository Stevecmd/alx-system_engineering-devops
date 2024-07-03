# Install and configure Nginx to meet specific requirements

# Ensure the system is updated
exec { 'update system':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin'],
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update system']
}

# Create the index.html file with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!'
}

# Configure the Redirect page
exec { 'insert_redirect':
  command => "sed -i '/rewrite ^\\/redirect_me https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4 permanent;/!24i\\rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
  unless  => "grep -q 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
  provider => shell,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Configure Nginx
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
