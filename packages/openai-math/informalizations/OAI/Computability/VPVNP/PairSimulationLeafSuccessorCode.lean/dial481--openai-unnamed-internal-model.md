---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSuccessorCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSuccessorCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native table for the successor fields at cursor zero

The first eleven registers are the shared incident-field mover. Registers
11–14 hold the dimension, last cursor, site, and site count. Register 16
holds zero. The three temporaries 17–19 hold the sender, mask, and class.


### `Stage`

 Control labels for testing outgoing and incoming endpoints, classifying the sender,
choosing a half-wire and copying its successor field. 

### `subRegs`

 Embed the incident-field mover's eleven registers in the first eleven slots of the
successor loader. 

### `classRegs`

 Wire the classifier's sender, unit, mask and class registers to successor-loader slots 17,
3, 18 and 19. 

### `port`

 Turn a selected side into the incoming or outgoing half-wire port, retaining an absent
selection at an endpoint. 

### `instruction`

 The successor-loader row at a given stage, from testing whether an edge exists through
choosing the source field and moving its bits. 

### `Linked`

 Each host instruction at a successor-loader stage implements its prescribed row using the
supplied register placement and exit. 

### `sender`

 The sending site index of an outgoing edge is the current index. For an incoming edge it is
the preceding index, with subtraction truncated at zero. 

### `active`

 Whether the indicated edge exists without wrapping. An incoming edge requires a positive
site index and outgoing requires a successor below the site count. 

### `selected`

 The low-bit successor class of the edge's sender, or no class at a missing nonwrapping
endpoint. 

### `useSide`

 The outgoing field uses the true side. The incoming field uses that side exactly for the
final successor class. 

### `sourceOffset`

 Offset of the selected successor field in its half-wire buffer, measured in blocks of eight
machine words' worth of bits. 

### `succBits`

 The eight-word successor field selected from the incoming or outgoing half-wire buffer,
with an all-zero field at a missing endpoint. 

### `Fixed`

 The shared mover and geometry registers hold the constants, half-wire bases, field length,
dimension and site coordinates required for successor selection. 

### `changed`

 Indices of the eight local registers that the successor-field selection and copy may
overwrite. 

### `Frame`

 Every host register outside the successor loader's eight writable slots agrees between the
input and output configurations. 
