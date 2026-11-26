---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSourceLocality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSourceLocality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSourceLocality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete source locality for the streamed head evaluation.
The source correspondence is `NodeConcrete.fixedSourceRow_baseline_eq` in
LeafProgramNodeConcretePlan, the actual residualJet in
LeafProgramNodeConcreteResidual, and residualProduct in
LeafProgramNodeConcreteResidualProduct. Fixed-high bits cancel in the full
integer signatures; every correction specialization uses one common U. 

### `baseline_locality`

 The actually stored baseline is equal under the owned-head bits and all
foreign full keys. Fixed-high coordinates cancel in the integer signatures. 

### `residualJet_locality`

 This is equality of the actual source jets before correction evaluation.
The missing-incidence branch is zero and the high branch is the common fixed bit. 

### `sourceProduct`

 The actual selected-factor product for one owned color group. IDs outside
the hash and optional marked range retain the original neutral-factor branch. 

### `sourceProduct_admissible`

 The actual retained source product has Boolean degree at most its Taylor
index, including the neutral-factor and empty-group cases. 

### `sourceProduct_coefficient_bounded`

 Every coefficient supplied to finite differences satisfies its precise
Taylor-degree bound; no restriction on J relative to the ambient size is used. 

### `colored_source_admissible`

 Admissibility of the actual product over all colored factor groups,
required by the grouped finite-difference query. 

### `sourceProduct_assignment_word`

 Source factor semantics read only the actual ambient assignment word;
all caches and physical scratch stacks are irrelevant to the polynomial. 

### `sourceProduct_locality`

 Whole selected group products agree as squarefree jets, before applying
the one shared correction U. All actual incidence rows use original IDs. 

### `sourceProduct_specialize_locality`

 Immediate specialization uses the identical U for both original
assignments; equality therefore survives the actual dense projection. 

### `stateFor`

 Canonical semantic state for the complete ambient assignment. Native
state comparisons need only identify its actual assignment word at145. 

### `colored_source_hlocal`

 Concrete hlocal for the actual colored selected-factor lists. Own-head
agreement and foreign full integer keys suffice; no evaluator, layout service,
or correction-dependent representative is assumed. 
