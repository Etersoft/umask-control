if [ -r /etc/sysconfig/umask.conf ]; then
	eval `grep 'umask' /etc/sysconfig/umask.conf` ||:
fi
