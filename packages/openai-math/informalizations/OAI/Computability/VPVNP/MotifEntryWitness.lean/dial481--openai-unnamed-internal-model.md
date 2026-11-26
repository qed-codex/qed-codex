---
{
  "module": "OAI/Computability/VPVNP/MotifEntryWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifEntryWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifEntryWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Monomial witnesses for fixed-motif entries

The successful entry of a local conversion map reads one parameter label
for every repeated base block. Its exponent vector counts these labels
with multiplicity. A failed entry has an empty choice type.


### `entryMultiplicity`

 Number of copies in which the entry reader returns a given parameter label. 

### `entryWitness`

 A successful entry has one witness, including when its specialized
coefficient is zero. All witness data are determined by the label list. 

### `entryWitness_totalExponent`

 Each accepted entry contributes exactly one label per base repetition. 
