---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedDirectoryHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedDirectoryHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedDirectoryHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placement directories in the final memory of a selected branch

A pass publishes its preimage arrays and input-header fields in its own
level and advances the successor's DFS base and role. Replaying subsequent
passes preserves the completed levels, including the occurrence-specific
directory of each selected term.


### `layers`

 The input layer followed by the actual output layers in the accumulated branch. 

### `Past`

 The directory arrays and their native header words in one memory.
The upper bound for each array is the next level, even though the common
traversal limit is the start of the DFS arena. 

### `Past.dirs`

 Placement directory of each previously selected level, as represented in the current raw
  memory. 

### `currentCount`

 Cardinality of the state where the next physical pass starts. 

### `Prefix`

 Past portion of the scheduled branch boundary. 

### `Past.transport`

 The terminal prefix may write its own table and header after the
completed directory region. Only the first 28 words of the final level are
needed to retain the selected DFS headers. 

### `Prefix.transfer`

 Live scheduler and row-launcher writes below the level arena leave the
past-directory portion of the branch boundary intact. 

### `Emission`

 The readback required at the completion of one native substep.
Its DFS prefix is advanced by the size of this input state; both words
written to the successor belong to the next pass's input header. 

### `Emission.dir`

 Placement directory published by the selected pass in its output memory, bounded by the
  next level's start. 

### `Prefix.empty`

 Initialize the DFS history from the published base and cursor role. 

### `Prefix.append`

 Extend the selected history by its actual pass. The new level can also
write the scheduler and the successor state. The proof only uses equality
on strictly earlier levels and the two carried words of its input header. 

### `Prefix.append_reports`

 A native report stream which writes only below the level arena or at
and above its own input level preserves every previously collected row. 

### `snapshot`

 Replay the first `j` packets, keeping their source boundaries. 

### `Retained`

 The accumulated directories of the actual selected execution. 

### `Retained.transport`

 Transport the full selected execution through the terminal prefix. 

### `Source`

 A batch of native reports which emits the selected occurrence and frames
all earlier levels, including when it also updates the low scheduler words. 

### `ofWalk`

 Extract every occurrence's directory at the final memory of the actual
report walk. Empty walks retain the cursor header. 
