#!/bin/sh

# Execute command (as non-root user)
exec su appuser -s /bin/sh -c "$*"
