---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack controls for Schur continuations

Ten independently tagged histories form one synchronized continuation stack.
The histories keep earlier frames intact through calls and returns. The routines
below require only the current ten live registers, and execute the same control
for every stack depth and register width.


### `push`

 Save all ten live fields into their respective history stacks. 

### `pop`

 Restore all ten fields of the most recently saved frame. 

### `histories`

 The newest saved field is first at every history port. 

### `push_data_runs`

 Save ten fields of arbitrary bit lengths; their lengths may differ by field. 

### `pop_data_runs`

 Restore ten fields of arbitrary bit lengths and leave their history tails intact. 

### `push_runs`

 Move one entire live continuation into the histories. 

### `pop_runs`

 Recover the saved direction, parent query, remaining summand and both scalars. 

### `history_length`

 The abstract call-stack depth directly bounds the bit height of each history port. 

### `push_space`

 Bit-space bound throughout a push, including instructions inside the field scans. 

### `pop_space`

 Bit-space bound throughout a pop, independent of the number of earlier calls. 
