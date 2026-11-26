---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpVectorEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpVectorEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpVectorEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Duplicate-free executable coefficient enumeration

These proofs concern the explicit lists used by `QuarticSearch`; they do not
replace the lists by an abstract enumeration of a finite type.


### `elements_nodup`

 The increasing residue representatives contain no duplicates, including
for a composite or zero modulus. 

### `vectors_nodup`

 Prefixing different alphabet entries gives disjoint blocks, while
prefixing one entry preserves the distinctness of the shorter vectors. 

### `allVectors_nodup`

 In particular the actual residue-vector search list is duplicate-free. 
