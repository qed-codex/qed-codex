---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleVisitor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleVisitor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryTupleVisitor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The representative tuple is already a polynomial-length stack of escaped
frames, deepest head first. These fixed commands copy that stack, extract one
actual representative, and decrement its unary physical head address. They do
not enumerate assignments or construct a Cartesian product. 

### `setup`

 The tuple remains on837 and its past-the-end head address remains on845.
The visitor borrows840 and843, which are empty at a complete tuple. 

### `readHead`

 Parsing restores the original little-endian representative, including
zero-width heads. The address pop is justified by its nonempty input below. 

### `setup_run_space`

 The visitor copies polynomial-length retained frame/address words once.
All persistent tuple and node accumulators are included in the initial bound. 

### `readHead_frames`

 The address counts unprocessed heads above the fixed node offset. Reading
one frame decrements exactly once, even if that representative has zero bits. 

### `readHead_frames_words`

 The native frame parser restores the exact stored representative rather
than constructing a coordinate tuple from arbitrary ring values. 

### `overwrite`

 Overwriting pays for removing the old word before copying the new one.
It is used for the persistent ambient representative baseline. 

### `testFrames`

 A peek checks whether another escaped frame exists. A zero-width head
still occupies its frame terminator and therefore enters the loop once. 

### `finishHead`

 The callback may consume or retain its parsed representative; clearing is
explicit and the next test is recomputed after its arbitrary register use. 

### `headBody`

 The instruction table is fixed; only the retained frame stack controls
its number of head visits. The same controller is used for both passes. 

### `FrameCursor`

 The source loop records only the remaining escaped frames and one unary
address. This is a proof predicate, not an executable list of visits. 

### `headLoop_eval`

 Composition over actual callbacks. This theorem charges every frame read,
representative clear and loop test. Concrete first/second pass callbacks must
instantiate its premise; it does not assert an evaluator implementation. 

### `overwriteState_bound`

 Repeated passes retain the same word bound: overwrite replaces one word,
rather than appending to a growing visit history. 

### `restart`

 Starting a second pass clears the previous node offset before installing
its past-the-end address. The retained representatives are copied unchanged. 

### `installRepresentative`

 The first tuple pass installs the current representative into the full
ambient baseline. The second pass can then retain every foreign head. 

### `installRepresentative_run_space`

 The concrete baseline update has a polynomial transient envelope and
returns to the same retained word bound, permitting repeated head visits. 

### `installedRepresentative_ofFn`

 The paid native update has the intended ambient-coordinate meaning;
foreign-head and fixed-high coordinates are read from the retained baseline. 
