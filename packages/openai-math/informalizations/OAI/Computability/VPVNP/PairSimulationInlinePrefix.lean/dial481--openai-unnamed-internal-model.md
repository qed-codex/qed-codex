---
{
  "module": "OAI/Computability/VPVNP/PairSimulationInlinePrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlinePrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlinePrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking lowered table prefixes into a larger native machine

The caller may place a continuation directly at an accepting exit and its own rejecting
instruction at a failure exit. A source prefix only executes nonterminal rows, so these
exit labels can be shared even when the source instruction at the exit is absent.


### `embedding`

 Install the consecutive source blocks and local registers at enclosing locations. 

### `Placement.withExits`

 A terminal source entry can be an external continuation label. Its outgoing row
is unnecessary when linking prefixes. 

### `continues`

 A nonterminal source row has a continuation. 

### `prefix_lower`

 Transport every local path, with the same choice bits and the exact fixed slowdown.
Only nonterminal code must be linked. The host's final configuration exposes the entire
source register file, the private memory, and the enclosing caller's register frame. 

### `ticks_lower`

 The map table's deterministic path and its computed histogram share the same private
memory. A bound on the source tick count scales by the uniform block length. 

### `restrict`

 View a live host configuration as source state at a known entry. 
