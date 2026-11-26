---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/States.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/States.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/States.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# State preservation by normalized multiplication

The order hypotheses here are the concrete tensor restriction properties. In
particular the lower bound on nonzero tensors proves the denominator is positive;
it is not a separate premise about a proposed character.


### `projective_mem_stateSet`

 Every projective map preserves all five defining state conditions, including
the detecting inequalities for every tensor. 

### `character_of_common_fixedPoint`

 A simultaneous fixed point of the actual state maps is a monotone semiring
character, and the detection inequality at the unit yields its required value. 
