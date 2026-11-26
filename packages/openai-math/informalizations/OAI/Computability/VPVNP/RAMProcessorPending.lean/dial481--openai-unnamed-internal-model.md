---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorPending.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPending.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPending.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External callbacks after a bounded private segment

The pending result uses the unspent fuel and the three probe allowances in
the physical bank. Connecting it to the internal scan preserves the full
report, including private choices that did not create memory records.


### `pending`

 Resume the native log program at a physical callback using the snapshot's remaining
instruction fuel, probe allowance and private choice stream. 

### `Meets`

 Specification of a physical run from a given label for a pending native result. Failure
reaches a rejecting row. Success reaches the iteration label with the matching report,
record buffer and unused choice suffix. 
