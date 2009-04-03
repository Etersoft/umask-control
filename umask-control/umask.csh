if ( -r /etc/umask.conf ) then
	eval `grep 'umask' /etc/umask.conf` ||:
endif
