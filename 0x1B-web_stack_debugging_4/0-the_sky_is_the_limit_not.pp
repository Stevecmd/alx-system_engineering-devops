# Update Requests Limit on Nginx to 4096

# Update Nginx configuration
exec { 'Nginx-Update':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Nginx Restart
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
