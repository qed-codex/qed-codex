---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramArrays.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramArrays.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramArrays.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical access to the two-array integer matrix ABI. Every array entry is a
runtime-width binary word; its signed value is positive minus negative. The
fixed program below preserves both arrays, the index and width. It does not
assume a unit-cost array lookup or add an integer primitive to the machine. 

### `readSignedCommand`

 Source arrays 0,1; preserved unary index 2; temporary index 3; preserved
unary width 4; positive/negative outputs 5,6; scratch 7--10. 

### `readSignedCommand_eval`

 The two signed components are read by actual preserving array scans.
No relation between the component magnitudes is needed. 

### `readSignedProgram_runsIn`

 Fixed-control primitive transition bound, including the final halt. 
