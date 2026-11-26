---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineOrdinalInversion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineOrdinalInversion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineOrdinalInversion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Recovering exactly the scheduled number of data-worker calls

The ordinal invariant determines when the guarded pass can close. Every
accepting online execution therefore runs the required number of source calls,
including when that number is zero. Its final data memory satisfies the last
ordinal invariant and preserves the descriptor control cells.


### `recover_ordinal_worker`

 The recovered source runs at its own cap, its call count is exactly
the selected ordinal interval, and its original data memory remains available
at the handoff to the calendar. 
