# Ensure the puppetlabs-stdlib module is installed

exec { 'fix_bad_extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  onlyif  => 'grep phpp /var/www/html/wp-settings.php',
}
