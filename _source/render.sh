#!/bin/bash
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
IN="$1"; W="$2"; H="$3"; OUT="$4"
TMP="${OUT%.png}@2x.png"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
  --force-device-scale-factor=2 --window-size="${W},${H}" \
  --virtual-time-budget=4000 --screenshot="$TMP" "file://$IN" >/dev/null 2>&1
sips -z "$H" "$W" "$TMP" --out "$OUT" >/dev/null 2>&1
rm -f "$TMP"
echo "rendered $OUT"
