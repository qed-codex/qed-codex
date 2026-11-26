---
{
  "module": "OAI/Computability/VPVNP/CompressorScheduledSlotRates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScheduledSlotRates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScheduledSlotRates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Charged work of the complete shrinking slot program

The seven preparation segments, nine slot and incidence segments, and six
canonical copy segments form the 22 visits of the fixed slot plan.
The copy also applies to the output of a port refresh.


### `copyColumns`

 Six canonical transfer passes for any selected output state. The first three
columns have one cell per base port and the remaining three one per actual port. 

### `slotRate`

 Coefficient per packed site, including the temporary owner holes, zeroed
counters, lane-lifted incidence columns and the six transfers. 

### `slotProgram`

 The 22 physical passes with their native reports. The two count equalities
are supplied by `ShrinkSlots.next_counts` for the actual selected output. 

### `selectedSlotProgram`

 The 22 visits on the selected dyadic branch, including the transfer of its actual
width column into the next level. The incoming position count pays for the whole run. 
