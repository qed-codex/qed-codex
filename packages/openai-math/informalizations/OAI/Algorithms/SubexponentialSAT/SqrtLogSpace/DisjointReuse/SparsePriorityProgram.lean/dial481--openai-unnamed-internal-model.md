---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete components of the sharp clause/core search from Appendix A.
The guard counts actual framed literals and executes the preserving subset tester.
The complete search and its polynomial resource bound are developed separately below. 

### `selectedRaw`

 Raw-list specification of the selected family; all runtime tests are bit programs below. 

### `masks`

 All masks have fixed length `k`; the finite control table depends only on `k`. 

### `select_none_of_raw_failure`

 Source-level negative evidence obtained after every finite candidate fails. 

### `RawPriority`

 A scan certificate records only tested candidates and preceding failed tests. 

### `copyClause`

 Only input-sized words are copied: the clause, its width, and the core. 

### `command`

 The core is on stack 8, clause on 9, and exact binary width on 10.
All eight work stacks are empty at both boundaries; register 12 receives the result. 

### `command_eval`

 Compare a scanned family's exact size with a binary threshold without expanding
that threshold to unary. The only unary count has length bounded by the input. 

### `command`

 The exponent depends only on the fixed width/core-size pass, before input quantification. 

### `copy`

 The primitive word operations use one fixed empty copy buffer. 

### `prepareCandidate`

 A failed candidate leaves both output ports empty; a successful one retains
its core and selected family. The surrounding parser owns ports 14 and 15. 

### `widthFamily`

 All three parameters are encoded in finite control before the input is supplied. 

### `higher_priority_mem_before`

 Every strictly preferable width/core-size phase occurs before a winning phase,
independently of mask and clause ties within that phase. 

### `command`

 One finite ordinary Boolean-stack program for each fixed width bound.
The outstanding proof obligations concern this concrete code, not an oracle callback. 

### `load_eval`

 Loading a fixed literal word touches only the low eight registers. 

### `selectedFamily_widthFamily`

 The two streaming reversals cancel. No family is duplicated in the output. 

### `scan_callback_contract`

 Failed callbacks restore the empty output banks. A successful callback
retains its actual output, and no further callback is required by the iterator. 
