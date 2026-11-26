---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The descriptor words of a resident six-party map

The selected term supplies its copy count and the eight payload widths.
The dense two-column demand array supplies AB and CD. Each absorbed role
reads its single shared private slot. The surviving roles read the buffers
assembled from subdivision frames. The CD endpoints read the stored old
half-wire directly, and AB reads its assembled bundle slice.


### `Arg`

 One descriptor slot of the map evaluator, indexed by a demand edge or one of the eight
supply roles where needed. 

### `Endpoint`

 A source or target half of a demand edge or supply role whose field buffer the six-party
map can read. 

### `Scratch`

 The eight surviving endpoint staging intervals follow the single AB interval.
Every absolute absorbed role has its own earlier interval, shared by its ends. 

### `Scratch.hidden`

 First private word reserved for absorbed supply labels shared by their two endpoints. 

### `Scratch.stride`

 Number of private words reserved for each shared or staged field. 

### `Scratch.motifs`

 Number of motifs for which the hidden pass reserves four shared field intervals apiece. 

### `Scratch.hist`

 Private base address of the label histogram updated by the map evaluator. 

### `Scratch.staging`

 Base of the AB buffer, immediately after the four shared intervals for each motif. 

### `Scratch.shared`

 Base of absorbed role `t`'s shared label in the four-field block for motif `ordinal`. 

### `Scratch.surviving`

 Base of role `t`'s staged surviving field at the chosen source or target end. 

### `Scratch.directory`

 Base of the lookup directory after the AB interval and the eight surviving endpoint
intervals. 

### `Scratch.descriptor`

 Base of the map descriptor following the sixteen directory words. 

### `Scratch.source`

 Start of the source-copy indices immediately after the complete descriptor. 

### `Scratch.target`

 Start of the target-copy indices after all source-copy indices. 

### `demandParty`

 The source party of a demand edge for an outgoing field and its target party for an
incoming field. 

### `supplyParty`

 The party incident to the specified supply role at its outgoing or incoming end. 

### `Scratch.fieldBase`

 Locate the endpoint at party `j` in its old CD, staged AB, surviving, or shared buffer. An
absent endpoint uses address zero. 

### `Inputs`

 Live operands: the canonical level header, the dense motif ordinal, the
private arena and the old CD source or target computed from its physical row. 

### `Inputs.level`

 Register expression for the producing level header from which the map loads its published
  addresses. 

### `Inputs.ordinal`

 Register expression for the selected motif number in the dense ordering. 

### `Inputs.hidden`

 Expression for the base of the shared absorbed-role buffers. 

### `Inputs.stride`

 Expression for the allocated width of each shared or staged buffer. 

### `Inputs.motifs`

 Expression for the number of motifs represented in the shared buffers. 

### `Inputs.hist`

 Expression for the private histogram base used to count selected map labels. 

### `Inputs.cd`

 Expressions for the old CD half-wire buffers at the source and target of the demand edge. 

### `loadHead`

 Load the word at a fixed offset from the producing level header. 

### `term`

 Compute this motif’s term-row address using the published term base, row stride and dense
ordinal. 

### `copies`

 Read the copy count from the second word of the selected term row. 

### `layout`

 Read the selected shrinking layout bit from offset 38 of the level header. 

### `demand`

 Load the AB or CD demand width in the two-word row for this motif. 

### `payload`

 Load the selected payload width at the recorded role index after the two leading term
words. 

### `staging`

 Compute the start of the AB staging interval beyond the four shared buffers for every
motif. 

### `shared`

 Compute the shared buffer address for absorbed role `t` of the current motif. 

### `surviving`

 Compute the staged buffer address for one of four surviving roles at the selected source or
target end. 

### `directory`

 Compute the lookup directory address after the nine staging intervals. 

### `descriptor`

 Compute the descriptor address immediately after the sixteen directory words. 

### `source`

 Compute the start of the source-copy indices after the descriptor slots. 

### `select`

 Selecting between the two field addresses works in the machine-word ring. 

### `base`

 Build the register expression selecting the actual input buffer for an incident endpoint,
using the recorded layout for supply roles. 

### `fields`

 Supply each descriptor slot of the selected party with its buffer address, size, copy count
or histogram pointer. 

### `Stored`

 Readback equations identifying the live register expressions and published header cells
with the selected motif, layout, term row and scratch allocation. 

### `values`

 The descriptor word at each argument slot for a given motif and party, using the selected
payload widths and fixed block repetition count. 

### `fields_eval`

 Every word to be written into the native call descriptor is read from the
chosen term, the true CD/AB demand record, or its designated private region. 
