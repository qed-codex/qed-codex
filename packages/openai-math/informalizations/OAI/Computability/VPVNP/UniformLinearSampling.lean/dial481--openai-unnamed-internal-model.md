---
{
  "module": "OAI/Computability/VPVNP/UniformLinearSampling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniformLinearSampling.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniformLinearSampling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform sampling through a surjective additive map

In Section 5.2, evaluation of a random linear map on a frame is a surjective
additive homomorphism. Translation invariance of finite group averages shows
that its image is uniformly distributed, including for simultaneous evaluation
on a frame spanning the two adjacent planes.


### `uniformAverage_comp_surjective`

 A surjective additive homomorphism carries the uniform distribution of the
finite domain to the uniform distribution of the codomain. 

### `frame_eval_surjective`

 Independent columns can be assigned arbitrary values by a linear map. 

### `uniformAverage_frame_eval`

 The joint images of any independent frame under a uniform linear map
have the uniform distribution on all tuples of target values. 
