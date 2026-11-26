---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpBaseNegation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBaseNegation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBaseNegation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary modular negation for fixed-width base coefficients

The data path creates a width-(B+1) zero shape, pads both operands, performs
the verified bitwise subtraction, reduces the difference, and normalizes to
B bits. Reduction is uniform, including x=0 and modulus=2^B. Encoded values
are never decoded by the algorithm. The event list records actual finite
bit/constructor operations; its length is not claimed to be a Turing runtime.


### `zerosLogged`

 Build a zero shape and record each emitted bit. 

### `takeLogged`

 Copy a bounded prefix, recording every copied bit. 

### `normalizeLogged`

 The same value as normalizeBits, with explicit shape/copy/padding events. 

### `negBaseLogged`

 Fixed-width negation using finite bit operations and uniform reduction. 

### `negBaseRun`

 API parallel to addBaseRun/mulBaseRun; the count is an actual log length. 

### `negBaseLogged_count_exact`

 Exact finite-event count; it does not depend on the encoded input value. 

### `negBaseLogged_count`

 A uniform polynomial bound on the length of the concrete emitted log. 

### `subtraction_trace`

 The subtraction portion has an actual measured finite-control trace. 
