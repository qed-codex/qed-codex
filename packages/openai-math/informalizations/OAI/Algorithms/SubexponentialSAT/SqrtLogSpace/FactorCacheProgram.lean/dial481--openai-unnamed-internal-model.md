---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorCacheProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorCacheProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorCacheProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical reconstruction of the exact node caches, including the sparse
ring identity and ambient shape, before accepted assignment evaluation. 

### `setupLocal`

 Clears stale copies, including ambient shape88, before reconstructing the
actual encoded ring identity69 and the idempotent coefficient tape143. 

### `setup_run_space`

 The setup trace includes the finite caller return. Its polynomial local
runtime accounts for every copy and temporary at every prefix. 

### `setup_low`

 All 56 arithmetic ports are restored to the original Product.idle ABI.
The other copied cache words lie outside that bank. 

### `setup_one_word`

 The word69 is constructed by the actual constant encoder, including the
ambient coordinate count. No semantically supplied ring-one dictionary is used. 

### `setup_cache_wordBound`

 The setup's retained cache bound depends on the original physical words,
not on a growing total-space envelope. All untouched caller words retain their
original bound. 

### `setup_cache_wordBound_max`

 The retained cache envelope uses physical master sizes separately from the
caller frame. Repeating setup therefore preserves any common bound containing
both the frame and the fixed generated cache words. 

### `setup_context`

 Concrete setup produces the same identity dictionary used by subsequent
factor semantics, with an exact frame for all non-cache caller storage. 
