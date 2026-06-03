#!/bin/sh

# Randomize FLASK_SECRET_KEY if unset
if [ -z $FLASK_SECRET_KEY ]; then
	export FLASK_SECRET_KEY=$(hexdump -vn16 -e'4/4 "%08X" 1 "\n"' /dev/urandom)
fi

# Execute command (as non-root user)
exec su appuser -s /bin/sh -c "$*"
