---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFieldParameterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldParameterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldParameterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual field-parameter arithmetic on binary stack words

The fixed program receives `p` and `delta` on stacks 0 and 1. Stacks 0--7
are retained logical words, and stacks 8--15 are an initially empty work bank.
All width bounds concern actual words, including any leading zero padding.


### `width`

 Explicit width parameter for arbitrary, possibly padded input words. 

### `core_eval`

 Four genuine multiplication calls and one decrement compute the field
size and denominator, preserving the actual input words. 

### `division_eval`

 Divide a copied numerator by the stored denominator. Both source words
survive unchanged and the temporary remainder is actually cleared. 

### `program`

 The instruction table depends only on the fixed parameter `k`. 

### `run_value`

 Actual halted execution, exact field-parameter values, retained-word
width bound, and empty scratch bank. 

### `primitive_value`

 Compilation to primitive tapes changes the bound by a constant depending
only on the fixed instruction table. 

### `run_polynomial`

 Bounds supplied by actual word producers yield a uniform polynomial
execution bound. In particular, the proof does not infer widths from values. 

### `Output`

 Concrete local endpoint contract, convenient for callers that lift this
stage into a larger persistent state. 
