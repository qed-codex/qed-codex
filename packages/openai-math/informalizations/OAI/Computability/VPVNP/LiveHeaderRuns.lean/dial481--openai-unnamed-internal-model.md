---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderRuns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sequential execution of the distributed index scan

The invariant states exactly what the six probes per call have read and
written. Addresses for the three scratch regions are disjoint from the site
headers. Thus the last call sees the real highest position and population
count, even for a group index much larger than the RAM word modulus.


### `run_cursor_segment_at`

 Consecutive deterministic microcalls realize a memory invariant after
each cursor and cost at most `probeBound + 1` per cursor. 

### `ScanLayout`

 The concrete scratch layout for one scan: original site words below
`length`, an unpacked array beginning at `pub 0`, then the two scalar cells. 

### `ScanInv`

 Exact invariant over the real external word memory after `cursor` cells. 

### `index_scan_native`

 The native `indexCell` table reads exactly the occupied index positions.
Its end state points to the next phase and each call costs seven calls-plus-probes. 
