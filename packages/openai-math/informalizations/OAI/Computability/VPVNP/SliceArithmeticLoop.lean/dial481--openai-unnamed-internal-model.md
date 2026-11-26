---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite-control counted scan of a coefficient stream

The register bank holds a stack of one-bit markers. Each marker causes one
normal execution of the same body. The body can update the accumulator and
advance all coefficient streams. The empty marker stack returns to the caller.


### `repeatMarked`

 Execute the body on each true marker, stopping normally on an empty stack. 

### `repeatMarked_runs`

 A fold over a represented stream uses at most one bounded body run and
one marker pop per item, plus the final test for the empty marker stack. 
