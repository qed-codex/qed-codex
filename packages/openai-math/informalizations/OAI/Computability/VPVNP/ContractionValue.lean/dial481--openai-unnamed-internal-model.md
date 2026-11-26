---
{
  "module": "OAI/Computability/VPVNP/ContractionValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ContractionValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ContractionValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Supremum of spectral values of center contractions

In the proof of Theorem 2.4 of *VP and VNP differ over every field*, the
center contraction may use any covector, including on products of several
wires. Its supremal spectral value is monotone under local restrictions.
Direct sums separate into independent blocks, and an embedded old factor
can be evaluated separately.


### `contractionValue`

 Supremum over all covectors on the center, before acting at the old parties. 

### `contractionValues_bddAbove`

 A common bound for all contractions depends only on the dimensions at the old parties. 

### `isLUB_contractionValue`

 The real least upper bound used in the root-limit estimates. 

### `contractionValue_mono`

 A restriction can only decrease the supremal contraction value. 

### `contractionValue_zero`

 Each contraction of a zero array is zero. 

### `contractionValue_unit`

 Contracting the unit by the all-ones covector attains the dimensional upper bound. 

### `one_le_contractionValue`

 A nonzero extended tensor has a center contraction of supremal value at least one. 

### `contractionValue_directSum`

 The two blocks of the center admit independent covectors, so the
supremum of contractions is additive on direct sums. 

### `contractionValue_le_extension`

 A spectral extension dominates every old contraction of an extended tensor. 

### `contractionValue_embedOld`

 The unit center leg on an embedded old tensor can be contracted with coefficient one. 

### `contractionValue_old_product`

 Embedded old tensors multiply the contraction value by their spectral value. 
