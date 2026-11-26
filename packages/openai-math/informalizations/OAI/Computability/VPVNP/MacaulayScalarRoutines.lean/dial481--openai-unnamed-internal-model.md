---
{
  "module": "OAI/Computability/VPVNP/MacaulayScalarRoutines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayScalarRoutines.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayScalarRoutines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Returning monomial-index and powered-entry routines

The caller supplies fixed-width registers and receives the raw index or
comparison flags in the same bank. Both routines return with the private log
and instruction scratch ports empty.


### `ordinalRoutine`

 Returning register routine that decodes a dense graded monomial ordinal to its raw code. 

### `exponentRoutine`

 Returning register routine that compares transformed source exponents with a column,
reports divisibility and equality, and reads a requested residual exponent. 
