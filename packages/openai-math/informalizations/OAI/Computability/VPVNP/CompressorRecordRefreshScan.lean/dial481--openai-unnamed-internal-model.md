---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete external-bundle pass of Appendix E

The segment scan visits all old actual arc numbers in increasing order. Each bundle's
accumulator is independent. Both endpoint arrays receive the prefix in source order and
the incoming array receives the source's width, including at an empty segment. The scan
runs from zeroed bundle totals and preserves the read-only directory and old widths.


### `Input`

 Directory and old wire lengths, in the word format used by `visit`. 

### `Input.width`

 The old outgoing width at each source-ordered segment ordinal. 

### `Input.target`

 The translated destination bundle number at each source bundle ordinal. 

### `Input.shift`

 The binary port displacement associated with each source bundle. 

### `Input.dest`

 Compute the destination segment ordinal from the immutable bundle target and port-shift
functions. 

### `prefixTotal`

 Width accumulated in a given bundle in the first `k` visits. 

### `cell`

 Read the indexed word of the table whose base is the selected public operand. 

### `Regions`

 The nonzero public indices name the seven arrays. All array indices are below `n`. 

### `Regions.packed`

 Seven consecutive arrays of the same capacity satisfy the address condition. 

### `Legal`

 `dest` permutes the scanned interval and all computed bundle totals fit in a word. 

### `LiveBundle`

 Exactly the directory entries reached by old outgoing slot identifiers. 

### `AtCursor`

 Physical contents at the scan cursor. Unvisited output entries may contain arbitrary
words. Every incoming entry below the cursor is keyed by the translated destination. 

### `AtCursor.start`

 At cursor zero only the old tables and zeroed bundle totals need initialization. 

### `AtCursor.exact`

 Under the one-word width bound the two offset cells carry the exact natural prefix. 

### `cursor_step`

 A native segment visit preserves the scan invariant. 

### `outsideScan`

 The external pass writes the total and three segment columns, indexed below `n`. 

### `scan_run`

 All native calls of the external scan and all records through the resulting cursor. 

### `scan_cost`

 The exact call-plus-probe cost through all visited segments. 
