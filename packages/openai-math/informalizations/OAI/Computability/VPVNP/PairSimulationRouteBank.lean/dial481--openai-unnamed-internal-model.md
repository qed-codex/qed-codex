---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed instruction bank for the complete cursor routing scan

Seven scheduler instructions, three three-instruction loops, and two
53-instruction field calls run the entire scan. The two exit labels may
be connected to the surrounding leaf program. The standalone table puts
accept and reject at these exits and requires no public data.


### `Control`

 Control labels in scheduler, successor, sorting-phase and sorting-step order. 

### `Call`

 Geometry, address selection, and the field-bit scan of one invocation. 

### `Body`

 The two field calls have separate return labels in the surrounding loops. 

### `Address`

 All instruction addresses, followed by the success and failure exits. 

### `program`

 Relocate all internal labels, both exits, and the register bank. 

### `text`

 Literal, word-width-independent instructions with the requested addresses. 

### `linked`

 The relocated body supplies every scheduler and field-call link. The
caller can install its own instructions at the two exit labels. 

### `locations`

 Numeric program counters 0–121 contain the body. Counters 122 and
123 are the successful and failed exits. 

### `canonical`

 Canonical allocation of the scan's 32 register slots and 124 labels. 

### `template`

 Complete finite program text, with terminal instructions at its exits. 

### `machine`

 Instantiate the same table at any host word width. 
