---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticStreamStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Staging the persistent streams of a Horner round

A fixed control copies the advised modulus, the multiplier and the row count
into the three consumable input stacks of the coefficient scan. All three
source stacks remain available for the next Horner digit.


### `Port`

 Ports for saved and consumable copies of the reduction coefficients, multiplier, and row
count, plus copy scratch space. 

### `stage`

 Three order-preserving copies into empty stacks. 

### `frame`

 State of the three saved streams and their three consumable input stacks for one Horner
round. 
