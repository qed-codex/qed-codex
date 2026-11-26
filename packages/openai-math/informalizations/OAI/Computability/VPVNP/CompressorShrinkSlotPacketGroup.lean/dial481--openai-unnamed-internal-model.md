---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotPacketGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotPacketGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotPacketGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packet groups from chronological source walks

The ordinal of a source packet is its position in the window, even when
two workers or two visits coincide. Each packet retains the source
segment's input memory, reports and tapes. An invariant can be carried
along the original report sequence to justify its launch operands.


### `with_invariant`

 Carry a memory invariant into the input of every source segment and
through the complete report log. 

### `with_agreement`

 An actual walk that writes only outside a region keeps the reference
memory's operands there at every packet start, and in the final memory. 

### `of_window_walk`

 Assemble a complete window from its actual runs. The certificate is
indexed by the label occurrence, so it can use that occurrence's physical
calendar ordinal directly. 
