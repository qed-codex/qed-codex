---
{
  "module": "OAI/Computability/VPVNP/SmallPrime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SmallPrime.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SmallPrime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A small characteristic preserving a nonzero integer minor

Section 8.2 of *VP and VNP differ over every field* needs a prime avoiding a
nonzero integer determinant. If the determinant has absolute value at most
`2 ^ B`, the prime may be taken at most `2 * (B + 2) ^ 2`. The elementary
estimate for the least common multiple of the first `n` integers gives this
polynomial bound directly.


### `exists_small_prime_not_dvd`

 A positive integer of at most `B + 1` binary digits has a nondividing
prime bounded quadratically in `B`. 

### `exists_small_prime_not_dvd_int`

 The integer minor stays nonzero modulo a prime with the same bound. 
