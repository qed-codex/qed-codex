---
{
  "module": "OAI/Computability/VPVNP/PairVertexLevelScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finding the producing level of a popped DFS node

The native program reads the starting row address of the last level and moves backwards
until the node lies at or above the current start. It uses one external read per tested
level. The successful exit computes the previous level header and the packed site number.


### `scan`

 Read the candidate level's DFS start, compare it with the popped node, and either finish or
step back one level. 

### `finish`

 Recover the old level, its child-header address, and the node's site ordinal from the
successful scan registers. 

### `testEvents`

 Events of one descending test, including the read of scalar 14 in the candidate level. 

### `scanEvents`

 Test the levels from `j + later` down through `j`, including the final test. 

### `ScanState`

 Register invariant of the descending locator, recording the popped node, terminal geometry,
and the level currently being tested. 

### `Frame`

 Frame condition preserving registers outside the locator bank, private memory, and
persistent state during level lookup. 

### `scan_run`

 Run the descending scan. Empty levels above the selected row are tested normally. 
