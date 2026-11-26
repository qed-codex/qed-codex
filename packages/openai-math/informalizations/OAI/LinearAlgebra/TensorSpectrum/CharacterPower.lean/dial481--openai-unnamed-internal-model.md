---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/CharacterPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/CharacterPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/CharacterPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The power law for a monotone multiplicative function

On the positive integers, a multiplicative, monotone real-valued function with
`1 ≤ f n ≤ n` is a real power.  No power representation is an input.  The proof
compares `n ^ k` with two successive powers of `m`; the resulting bounded error
forces the logarithmic slopes to agree by the Archimedean property.


### `monotone_multiplicative_log_cross_le`

 Monotonicity and multiplicativity force equal logarithmic slopes.
The orientation here is useful without dividing by either logarithm. 

### `exists_power_of_monotone_multiplicative`

 Every monotone multiplicative function between `1` and the identity on the
positive natural numbers has a single exponent in `[0,1]`.  There is no
restriction on its unused value at zero. 
