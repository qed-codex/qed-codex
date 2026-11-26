---
{
  "module": "OAI/Computability/VPVNP/MacaulayOrdinary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayOrdinary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayOrdinary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The fixed scalar-entry program for the augmented Macaulay matrix

All three arms run literal finite stack programs. The original row evaluates
two signed counts, the affine row consults the pin table, and the appended
row compares its powered source monomial with the column. Matrix dimensions,
scalar field data, and coefficient circuits enter only through the caller's
stack bank.


### `ordinaryArms`

 The three scalar-entry routines. Equation rows use signed counts, affine rows use pin
advice, and powered rows compare exponent vectors. 

### `ordinaryReader`

 Fixed row decoder and dispatch program with the equation, affine and powered scalar-entry
arms installed. 
