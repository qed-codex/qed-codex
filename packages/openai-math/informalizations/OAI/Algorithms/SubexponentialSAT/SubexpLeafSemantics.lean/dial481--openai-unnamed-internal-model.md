---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLeafSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLeafSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLeafSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed sparse-leaf semantics at the actual finalizer boundary

The byte test below is a finite reference computation used only in the
correctness statement. The fast callback obtains its answer from the actual
moment, reconstruction, and finalizer programs. No execution or fast bound
for this reference decoder/search is asserted.


### `test`

 A reference answer on bytes. It is never used as a machine instruction. 

### `validPayload`

 The logical property of leaves may be the actual sparsifier invariant.
The encoding witnesses preserve the complete observed list order. 

### `finalize_execution`

 This invokes the real finalizer on the single H(0) quartet. The caller
must still provide its actual reconstruction denotation and input state. 
