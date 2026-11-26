---
{
  "module": "OAI/Computability/VPVNP/GrassmannWalkTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannWalkTransfer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannWalkTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Passing the strict Grassmann inequality to a sparse walk

Average the strict Grassmann inequality over the random linear map. The two
marginal laws needed here are independence on complementary planes and
independence within matching fibers on adjacent planes. All averages are
finite sums. The vertex factor in the conclusion agrees with the walk energy
normalization in Section 5.2.


### `expectation`

 Uniform expectation over a finite sample space. 

### `PairSamplingLaws`

 The two finite marginal distributions of the linear-map sampling experiment.
Each equation quantifies over all observables, independently of the metric target. 

### `PairSamplingLaws.transfer`

 Average a Grassmann inequality over the sample space and use the pair
laws to identify its left side with the uniform all-pairs energy. 

### `PairSamplingLaws.sparseBound`

 Given the marginal laws of the random linear map, the actual fiber and
permutation mixture has the recursive Poincaré coefficient of Section 5.2. 
