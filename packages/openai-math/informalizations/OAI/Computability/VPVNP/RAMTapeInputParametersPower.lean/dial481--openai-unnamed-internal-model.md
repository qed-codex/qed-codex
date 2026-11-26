---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary powers for the live bucket exponent

The fixed numerator of the rational exponent is a finite loop bound.
Each iteration copies the base, calls the word multiplier, and restores
the product to its input port for the next call. The word width is supplied
by the stacks and is independent of the number of control states.


### `Port`

 Ports for the power routine’s base, temporary reversal, and multiplication registers. 

### `Round`

 Phases of one power round, from copying the base through multiplication to moving the
product into the next accumulator. 

### `State`

 Power control carrying a bounded number of remaining rounds and the current multiplication
phase. 

### `code`

 Repeat multiplication by a restored copy of the base and transfer each product to the
accumulator for the next round. 

### `store`

 Initialize the base and temporary stack together with the accumulator, factor, and product
of the embedded multiplier. 

### `round_run`

 One round costs a quadratic number of bit operations and leaves the base available. 

### `power_run`

 The full fixed power loop works at every bit width, including zero width. 
