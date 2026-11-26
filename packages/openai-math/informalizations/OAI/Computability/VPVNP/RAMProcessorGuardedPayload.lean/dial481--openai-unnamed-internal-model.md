---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGuardedPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGuardedPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGuardedPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A deterministic payload after a two-exit processor fragment

A successful test enters the payload without an extra transition. Rejection
jumps directly to its caller label, leaving the rejected branch's stack state
available to the caller.


### `withPayload`

 Link a Boolean guard to a returning payload. Success enters the payload and a failed guard
transfers directly to the rejection label. 
