---
{
  "module": "OAI/Computability/VPVNP/CursorValidatorContraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorValidatorContraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorValidatorContraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local path counts at cursor zero

In Section 12 of *VP and VNP differ over every field* the selected outgoing and
returning fields at cursor zero supply the incident bits of the local RAM
validator. Successor fields use their unique active mask class, and a missing
successor at either endpoint supplies zero. Sorting layers have a field in
each direction. We identify this local decoder with the physical bit layout.


### `RAMPayload`

 All mask-system fields on one selected side of a cursor site. 

### `decodeSlot`

 Decode one incident slot using only the two sets of fields delivered to
this site's validator. 

### `decodeIncident`

 Serialize the decoded slots in the order expected by the RAM validator. 

### `decodeIncident_ram`

 For a routed assignment, the local decoder reads exactly the bit vector
at the corresponding site of the original transcript. 

### `validatorPaths`

 The genuine accepting private strings for the supplied local cursor bits. 

### `validatorPaths_sum`

 Summing the zero-cursor local counts against the physical sender arrays
gives the capped path count, with every private choice retaining its own
multiplicity. 

### `validatorNetwork`

 The initial network of Section 12 has a bit field for every RAM mask
system on each of the two arcs leaving each cursor position. 

### `initialChoices`

 A valid transit vertex contributes its unique empty choice. At cursor
zero the local choices are the private binary paths of the site validator. 

### `initialChoices_contract`

 The actual finite cursor network contracts to the capped RAM path count.
The local factor is defined for every half-wire input, even those that never
occur in a globally tied assignment. 

### `expandedRAMCount`

 Equation (12.2) for the paper's cursor graph, including any required
parallel zero-width slots. Given an exact finite compression history, the sum
of the monomials on its expanded paths equals the capped machine count. 
