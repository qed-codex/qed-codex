---
{
  "module": "OAI/Computability/VPVNP/PairShrinkPartyNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the selected resident shrinking-party columns

The packed old assignments determine each AB source bit, and one stored
parent packet supplies every incident surviving column. The selected row
allocation and ordered-slot table determine the pointer computations.


### `Job`

 The current map job uses the selected branch and the same arena for its old
child packets and its new half-wire packet. The three slice bases are public. 

### `Job.old`

 Placed old half-wire assignments at the resident party site, used to recover the demand
  operands. 

### `Job.parent`

 The selected output site's independent half-wire assignment supplying the subdivided
  surviving fields in its packet. 

### `Job.arena`

 Private argument arena shared by this parent packet and the old child packets. 

### `Job.node`

 Absolute DFS row address indexing the parent argument packet. 

### `Job.scratch`

 Private shared-field, staging, directory, and histogram addresses of this party's shrink
  map. 

### `Job.older`

 Start of the input layer's DFS rows, from which the old-site node addresses are computed. 

### `Job.pitch`

 Number of words per old DFS site row. 

### `Job.first`

 Start of the external AB frame-bank rectangle, with one indexed bank per bundle. 

### `Job.term`

 External base word for the selected shrinking term records. 

### `Job.stride`

 Word stride between successive dense motif term records. 

### `Job.widthBase`

 External base address of the surviving slice-width arrays in the selected allocation. 

### `Job.nodes`

 Locate an old site's child row using its site ordinal and the old layer's base and pitch. 

### `Job.abHalf`

 At A or B, extract the placed old half-wire assignment used by the indicated end of the AB
demand. 

### `Job.half`

 Transport the resident parent's half-wire assignment to the equal site at the chosen end of
a surviving supply wire. 

### `Job.allocation`

 The selected slice allocation determined by the term records, width base, and subdivision
profile for this shrink. 

### `Job.abRow`

 Copy row for one old AB arc, with its child packet as source and the party's AB staging
word as destination. 

### `Job.supplyRow`

 Reverse-copy row for one subdivision of an incident surviving supply field, read from the
parent packet and placed in its unsplit staging word. 

### `Job.row`

 Concrete field, address, offsets and bits at every visit of the party scan. 

### `Job.Packets`

 All input packet cells lie before staging and all staged widths fit their designated strides. 

### `supplyInputs`

 Construct the surviving gather operands for one orientation and role using the old level,
motif, parent node, and the role's staging destination. 

### `setups`

 Generate the native register setup for each active AB or surviving copy at this party,
using the old and new degree exponents. 

### `Job.OldPublished`

 Old-level columns, ranked original ID lists and the selected AB interval bank. 

### `Job.SupplyPublished`

 The common selected slot and interval images. The per-endpoint destinations are the
staging expressions in the very same six-party call header. 

### `Job.Assembled`

 Values consumed by the demand and supply map readers after all frames execute. 

### `Job.updated`

 The native update restricted to the upper private scratch. 

### `Job.trace`

 The public trace of a fixed resident job. 

### `native_party_reads`

 The installed rows return the typed map fields, the exact chronological trace and the
upper-scratch update. Private cells below the stack boundary are preserved. 

### `native_party`

 Run every real AB and surviving frame of the selected resident map, in one linked program.
The resulting private state supplies the bits of its typed matrix call. 
