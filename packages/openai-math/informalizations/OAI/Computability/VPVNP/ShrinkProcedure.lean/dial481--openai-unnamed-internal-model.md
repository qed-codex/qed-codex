---
{
  "module": "OAI/Computability/VPVNP/ShrinkProcedure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkProcedure.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkProcedure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running a shrinking template at one scheduled degree

The template and scheduled degrees are fixed before the coefficient ring,
its parameter assignment, the network and the number of remaining lanes.
The exact shrinking pass has the position divisor and energy multiplier
required to compose one block of Theorem 7.1.


### `shrinkRoundingError`

 The additive coefficient for this degree transition, before choosing
any solution of the fixed scalar equations. 

### `shrinkPassAt`

 The actual pass at any input lane length equal to the scheduled one. 

### `shrinkProcedure`

 An elementary scheduled shrinking procedure with the exact six-party
expansion in every term and the bounds of (7.2). 

### `shrinkProcedure_error`

 The same additive error works over every ring and for every solution. 
