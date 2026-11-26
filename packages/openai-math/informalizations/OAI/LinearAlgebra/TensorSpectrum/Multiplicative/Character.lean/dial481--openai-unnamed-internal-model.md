---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Character.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Character.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Character.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multiplicativity of a compact convex tensor-state space

This is Appendix A.2, including the single-map fixed-point existence step.
The projective fixed-point result is proved by finite weighted orbit averages,
so no Schauder theorem is postulated. Nonemptiness of the additive state space
is the explicit Appendix A.1 input; no multiplicative state is an input.


### `exists_character_of_nonempty_stateSet`

 Appendix A.2 turns an actual nonempty additive detecting state space into a
monotone real semiring character without assuming a character or fixed point. 

### `exists_nnreal_character_of_nonempty_stateSet`

 The same character with its nonnegative codomain made explicit. 
