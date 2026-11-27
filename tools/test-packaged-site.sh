#!/usr/bin/env bash
# Replay the browser fixtures against the ordinary and discussion-enabled packages.
set -eu
site=$1
discussion=$2
database=$3
fixtures=$4
export WRANGLER_SEND_METRICS=false QED_TEST_DATABASE="$database"
origin=http://127.0.0.1:18741
discussion_origin=http://127.0.0.1:18742
node_modules/.bin/wrangler pages dev "$site" --ip 127.0.0.1 --port 18741 --inspector-port 19841 --persist-to build/check-site-state >build/check-site.log 2>&1 &
site_pid=$!
node_modules/.bin/wrangler pages dev "$discussion" --ip 127.0.0.1 --port 18742 --inspector-port 19842 --persist-to build/check-discussion-state >build/check-discussion.log 2>&1 &
discussion_pid=$!
trap 'kill "$site_pid" "$discussion_pid" 2>/dev/null || true' EXIT
for address in "$origin" "$discussion_origin"; do
  curl --fail --silent --show-error --retry 20 --retry-connrefused --retry-delay 1 "$address/proof.json" >/dev/null
done
failed=0
for check in console directory map-links origin package-pages; do
  if [[ "$check" == directory ]]; then
    node tools/test-directory.mjs "$origin" "$database" || failed=1
  else
    node "tools/test-$check.mjs" "$origin" || failed=1
  fi
done
node tools/test-search.mjs "$origin" "$fixtures" || failed=1
node tools/test-launch-discussion.mjs "$discussion_origin" --fixture || failed=1
exit "$failed"
