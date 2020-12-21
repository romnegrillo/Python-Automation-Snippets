class ntp {
  package { "ntp":
    ensure => latest,
  }
}

include ntp
