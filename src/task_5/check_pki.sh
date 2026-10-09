#!/bin/bash
BASE="pki"
FILES=("certs/CAcert.crt" "private/CAkey.key" "newcerts/server.csr" "certs/server.crt")
for f in "${FILES[@]}"; do
  if [ -f "$BASE/$f" ]; then
    echo "OK: $f"
  else
    echo "MISSING: $f"
  fi
done
