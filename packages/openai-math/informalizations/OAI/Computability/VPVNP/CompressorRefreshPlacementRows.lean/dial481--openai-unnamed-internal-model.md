---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshPlacementRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPlacementRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPlacementRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical immediate-preimage rows of a degree refresh

The promoted port keeps its old site ordinal. One reset call per site
writes its owner, the singleton list length and the old identifier in
the corresponding child row. The resulting tables feed the same traversal
reader as the shrinking placement tables. The scan initializes each live
cell explicitly, irrespective of its initial contents.


### `code`

 Three public array bases, each with a unit stride. 

### `worker`

 Scheduled worker that writes one promoted site's owner, singleton preimage length and child
identifier from its cursor. 

### `bank`

 Select the three destination heads from operand positions one, three and five of the
refresh placement packet. 

### `cell`

 Word address of one site's entry in the selected owner, length or child array. 

### `value`

 Value written for this site. The owner and sole child receive its ordinal, and the preimage
length receives one. 

### `events`

 Exact private ticks and three external writes that install the singleton preimage row at
cursor i. 

### `report`

 The placement worker's write trace and its returned successor cursor i+1. 

### `log`

 Consecutive placement reports for the indicated number of sites, starting at cursor k. 

### `collected`

 The post-memory has the complete ordered list at each new identifier,
and every address outside the three placement arrays keeps its old value. 
