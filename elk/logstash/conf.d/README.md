# Tips for log sources

## VCSA
To get the logs out of VCSA in a very easy parseable format:
* From the VCSA web management console enable logging to a remote loghost and put * as the type of logs (or less if you don't want to receive everything that VCSA logs)
* From the CLI, start the shell and edit /etc/vmware-syslog/syslog.conf and edit the line about your syslog server and remove the __;RSYSLOG_SyslogProtocol23Format__ string at the end
* Restart the rsyslog service (__systemctl restart rsyslog__)

## ESXi
ESXi has all logs set to __verbose__ and it logs huge amounts of unnecessary data.
Set all logs to __warning__ and only the relevant logs will be sent over syslog
