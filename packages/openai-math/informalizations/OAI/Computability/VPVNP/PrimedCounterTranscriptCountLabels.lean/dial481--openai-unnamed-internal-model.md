---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterTranscriptCountLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTranscriptCountLabels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTranscriptCountLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded nominations and initial header words

A fixed-width nomination gives one natural exponent for each grammar label.
Its finite-support exponent vector is the monomial tested by the pair counter.
The external-memory initializer supplies its dense word table after the header
bits and uses zero elsewhere.


### `exponents`

 The monomial indexed by the complete nomination of label counts. 

### `coeff_exponents`

 Matching the nominated monomial has precisely the multiplicity of (9.4). 

### `ofNomination`

 Supply every nominated count from its fixed-width field to the parser. 

### `initialMemory_eq`

 Initializing the native validator's memory from the header-provider words
recovers all prescribed histogram components and zeros above the header. 
