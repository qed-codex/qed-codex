---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Incident external words in the degree refresh

In Section 7.3 of *VP and VNP differ over every field*, each destination slot
receives all its segments in one external word, ordered by the original source
ports. This gives a local evaluator of the two segment lists at every port and
identifies the widths used by its internal tensor with the widths in the energy
estimate.


### `oldPortMatching_symm_apply`

 The destination slot determines the incoming bundle. Invert its port
translation to recover the segment's position in the source ordering. 

### `oldPortMatching_bundle`

 Every old port in the same external word reaches the same block and slot. 

### `portSegments_eq_incident`

 At an actual port the segment lists in the old tensor can be read from the
two incident external words, using the same local reader as the kernel step. 

### `actualTarget_external_bundle`

 The actual refreshed matching sends the outgoing external word at a port
to the unique incoming external slot in the translated block. 

### `actualTarget_symm_external_bundle`

 The incoming word used by the local evaluator belongs to the actual arc
ending at the port's external slot. 

### `actualWidth_external_bundle`

 The external arc's actual width is the sum of the widths in its word. 

### `internalWidth_eq_tieWidth`

 For the actual matching, every internal tensor factor has the bit width
charged to the corresponding tie by the energy inequality. 
