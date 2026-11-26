---
{
  "module": "OAI/Computability/VPVNP/StructuredStackSafe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackSafe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackSafe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A space invariant on every branch of a returning stack routine

The caller checks its own invariant at a normal return. At each active
instruction the callee checks the current bank and both successors of a
binary choice. This gives a simultaneous clock and peak-space contract.


### `SafeFrom`

 Every branch from the given local control checks the stack invariant at each active
instruction and reaches a halt or a return within the fuel budget. At a return the
continuation receives the remaining fuel and stack bank. 

### `Safe`

 The all-branches stack invariant and fuel bound for a routine started at its entry label. 

### `SafeFrom.reach`

 Every reachable bank satisfies the invariant, including a normal return
when the caller's continuation enforces it there. 
