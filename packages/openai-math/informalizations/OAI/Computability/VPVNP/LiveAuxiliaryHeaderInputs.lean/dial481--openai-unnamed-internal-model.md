---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryHeaderInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking the seven input arrays to the auxiliary coefficient machine

The sparse writer reads one word per length, primed index bit, advice bit,
exterior bit, and nominated histogram entry. The field equations below
are the contracts provided by their individual producer routines.


### `fieldSize`

 The seven field lengths in copy order, covering the three length words, both index fields,
advice, exterior cuts, and nominated histogram. 

### `InputArrays`

 Memory equations for the producer outputs, before writing the sparse O header. 

### `InputArrays.read`

 Every packed read lands on its producer's word and every destination is
the address the auxiliary machine will query for that field. 
