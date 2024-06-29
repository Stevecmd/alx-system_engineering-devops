include stdlib

# Ensure password authentication is turned off for SSH
file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}

# Set the default identity file (private key) for SSH connections
file_line { 'Declare identity file':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true,
}
