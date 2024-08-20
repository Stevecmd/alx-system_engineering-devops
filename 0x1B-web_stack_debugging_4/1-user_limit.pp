# Update limits placed on Holberton User

#Increase Hard limit
exec {'Limit-increase-Hard':
  command => 'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase Soft limit.
exec {'Limit-increase-Soft':
  command => 'sed -i "/holberton soft/s/4/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
