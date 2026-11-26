---
{
  "module": "OAI/Computability/VPVNP/FixedProgramTailInitialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailInitialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailInitialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed diagonal program's native initialization function

The scalar evaluator and the physical midpoint store each exponent in the
same finite word width. Their complete initialization functions agree on
arbitrary natural inputs, including inputs reduced modulo that width.


### `nativeRuntimeNat_eq`

 Both ordinal maps select the same input coordinate, even when the
natural number supplied there requires reduction to the exponent width. 

### `midpointInitial_heq`

 The initializer of the physical tail continuation is the initializer
of the scalar model, with only the two equal index sizes transported. 
