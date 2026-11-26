---
{
  "module": "OAI/Computability/VPVNP/SpectralRelabel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralRelabel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralRelabel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relabeling the parties of a spectral point

In Lemma 2.3 of *VP and VNP differ over every field*, the parties used by a
fixed pattern of labels are identified across different realizations. A
bijection of party sets transports all local restrictions and both tensor
operations, so it gives a spectral point with the corresponding wire distances.


### `relabelTensor`

 Use a bijection to rename every party of a tensor. The finite local bases
are the same bases, indexed by the new party names. 

### `applyLocal_relabel`

 Local contractions agree after reindexing the sum of basis assignments and
the product of local matrix entries. 

### `relabel`

 Pull a spectral point back along a bijection of its party labels. 

### `wireDistance_relabel`

 Wire distances follow the party labels under a bijection. 
