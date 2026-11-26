---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackEngineAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking the Schur determinant callbacks

A single shared binary register bank computes child queries. Its output words
are copied into the emptied live registers only after the parent's frame has
been saved. The accumulator callback uses the native extension-field arithmetic.
The remaining installation point reads and interprets the matrix descriptor.


### `source`

 Auxiliary stack holding one pending child-query word in the dispatcher's output register
bank. 

### `actions`

 Link the descriptor, child dispatcher, activation and field multiply-add routines into the
evaluator's actions. 

### `Ready`

 The descriptor's additional state occupies ports outside the shared
Schur register bank. The field-arithmetic advice and scratch also persist. 

### `Pending`

 The auxiliary bank is ready and its six pending output registers encode the specified Schur
key. 

### `localBudget`

 Step allowance for local child dispatch, scalar multiply-add and movement of the encoded
words. 

### `contracts`

 Every call except the descriptor is instantiated here with an executable
finite bit-stack routine. The descriptor may have a separate, larger clock. 
