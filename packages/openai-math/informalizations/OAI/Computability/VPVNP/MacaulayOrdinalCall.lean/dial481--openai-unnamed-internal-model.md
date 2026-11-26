---
{
  "module": "OAI/Computability/VPVNP/MacaulayOrdinalCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayOrdinalCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayOrdinalCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A returning raw-key lookup which preserves the caller's ordinal and advice 

### `wordPorts`

 Between register instructions only the register and persistent ports
can be occupied. The instruction work ports and private log are empty. 

### `ordinal`

 Return the raw key of the requested source or column monomial while preserving the caller's
ordinal and parameter words. 

### `ordinalWork`

 Time allowance for copying the ordinal scan's input words, returning its raw key and
clearing the private scan bank. 

### `ordinalSpace`

 Stack allowance for staging and running one ordinal scan with register width w and caller
stacks bounded by B. 

### `ordinalClock`

 Tick bound for a complete bounded-degree ordinal search, including the private call's input
and output copies. 
