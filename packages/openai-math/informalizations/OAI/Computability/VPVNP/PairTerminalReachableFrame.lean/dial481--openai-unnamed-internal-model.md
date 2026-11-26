---
{
  "module": "OAI/Computability/VPVNP/PairTerminalReachableFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalReachableFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalReachableFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Protecting a live word on every reached call of the terminal program

The forced startup, prefix and traversal blocks reach the physical bit-scan
memory. The remaining two worker controls apply to every successful call,
including histories which a later site rejects.


### `QuietPrefix.choices`

 All branch tapes supplied to the three deterministic setup phases, in call order. 

### `QuietPrefix.logs`

 The original worker reports paired with their terminal-controller entries. 

### `QuietPrefix.reportList`

 The physical reports after the controller has wrapped every setup call. 

### `QuietPrefix.preservesCell`

 The protected-address property includes both continuing calls and the
last accepting exit. The setup frame is measured on its actual memory at
each report. The vertex invariant may depend on the fourth block. 
