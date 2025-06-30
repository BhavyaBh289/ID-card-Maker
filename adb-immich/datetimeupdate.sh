#!/bin/bash

# Usage: ./update_all_timestamps.sh [optional-folder]
TARGET_DIR="${1:-.}"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: '$TARGET_DIR' is not a valid directory."
  exit 1
fi

echo "Processing files in: $TARGET_DIR"

shopt -s nullglob
cd "$TARGET_DIR"

for FILE in *[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]*; do
  BASENAME=$(basename "$FILE")

  if [[ "$BASENAME" =~ ([0-9]{8})_([0-9]{6}) ]]; then
    DATE="${BASH_REMATCH[1]}"
    TIME="${BASH_REMATCH[2]}"
    TOUCH_TIME="${DATE}${TIME:0:4}.${TIME:4:2}"

    echo "→ Updating '$FILE' to ${DATE} ${TIME:0:2}:${TIME:2:2}:${TIME:4:2}"
    touch -t "$TOUCH_TIME" "$FILE"

    # macOS: Also set creation date
    if [[ "$OSTYPE" == "darwin"* ]]; then
      CREATION_TIME="${DATE:0:4}-${DATE:4:2}-${DATE:6:2} ${TIME:0:2}:${TIME:2:2}:${TIME:4:2}"
      SetFile -d "$CREATION_TIME" "$FILE" && echo "   ↳ Creation time set (macOS only)"
    fi

  else
    echo "Skipping '$FILE': filename does not match expected format."
  fi
done
