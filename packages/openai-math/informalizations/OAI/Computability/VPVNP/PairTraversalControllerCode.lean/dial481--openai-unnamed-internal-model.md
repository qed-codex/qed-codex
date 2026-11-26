---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native dispatcher for traversal table construction

Each reset entry loads the square base, radix exponent and persistent ordinal,
then computes the fixed operand formulas. Four comparisons dispatch to a role
write, a leaf header, a fiber translation, a phase reset or final acceptance.
All three workers return to the common successor-ordinal instruction.


### `P`

 Total program-counter count for the traversal controller's prelude, setup, guard, three
worker blocks, and four exits. 

### `preludePC`

 Place the traversal controller's three prelude instructions at their physical addresses. 

### `guardPC`

 Program counters of the guard that chooses the current traversal worker or an exit. 

### `setupPC`

 Place a register-setup instruction by its ordinal, falling through to the first guard when
setup is complete. 

### `rolePC`

 Physical instruction address in the role-tag writer's linked worker block. 

### `leafPC`

 Physical instruction address in the leaf-row writer's linked worker block. 

### `fiberPC`

 Physical instruction address in the worker that writes a site's selected placement fiber. 

### `nextPC`

 Exit returning the controller state for the next active site. 

### `resetPC`

 Exit that resets the site ordinal and advances to the next phase-level. 

### `acceptPC`

 Accepting exit of the completed traversal controller. 

### `rejectPC`

 Rejection exit reserved in the traversal controller's instruction table. 

### `table`

 One finite template for all inputs, word widths, layer counts and term choices. 

### `machine`

 Instantiate the fixed traversal controller template at the supplied word width and eleven
public operands. 

### `loaded`

 Configuration received by the formula evaluator immediately after reset. 

### `enter`

 The prelude takes exactly three ticks and reaches the first setup instruction
with its public and persistent inputs in registers. 

### `Route`

 Destination selected by the native tests after the formula evaluator. 

### `route`

 Choose acceptance, phase reset, or the role, leaf, or fiber worker from the decoded
phase-level and site bounds. 

### `Route.pc`

 Program counter entered after the guard has determined the traversal route. 

### `Route.ticks`

 Number of guard ticks before reaching the selected worker or exit, ranging from one at
acceptance to four at a descriptor worker. 

### `dispatch`

 Every guard contributes one tick and leaves the operand bank and both
memories available to the selected worker or exit instruction. 
