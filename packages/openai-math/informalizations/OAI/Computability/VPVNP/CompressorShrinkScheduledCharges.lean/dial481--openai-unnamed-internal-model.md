---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScheduledCharges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledCharges.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledCharges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Tapes and traffic of the three shrinking output windows

The native AB, surviving-width, ordered-slot and canonical-copy reports all
consume empty tapes. We count the calls of each scan and include the actual
copy reports in the bound per incoming wire position. The same statements
hold for the packet choices whenever the packets replay these reports.


### `rate`

 Incoming positions pay for the AB and width rectangles, and for the
ordered-slot scans and their physical transfers. All three rates depend
only on the fixed degrees and the subdivisions of the template. 

### `Accounted`

 Counts, costs and choice tapes for the four report lists in Parts 6–8. 

### `accounted`

 Account for the reports of a completed three-table run and the six copies
which follow it in the ordered-slot window. 

### `Accounted.exact_cost`

 The AB intersection probes depend on the widths. Once that observed charge
is fixed, the remaining three scans have the following exact charge. 

### `Accounted.packets`

 The actual packet tapes and their source charge for the concatenation of
all three windows. The only input about the packets is their verified native
chronology and the equality of the four flattened report lists. 
