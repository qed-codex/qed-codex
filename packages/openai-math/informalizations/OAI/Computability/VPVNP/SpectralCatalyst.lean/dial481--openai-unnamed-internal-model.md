---
{
  "module": "OAI/Computability/VPVNP/SpectralCatalyst.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCatalyst.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCatalyst.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Removing additive slack in strict spectral comparison

Appendix A.1 obtains a comparison with a common summand after clearing
denominators. Trading multiple copies absorbs that summand and leaves a
single multiplicative catalyst. Its size bounds the number of copies needed
for all tensor powers simultaneously.


### `remove_additive_slack`

 A common summand in the comparison between `(b+1)cX` and `bcY` can
be traded away by taking `q` copies, with `q c Y` large enough to cover it. 

### `catalyst_powers`

 The same catalyst can be reused once per factor of a tensor power. 

### `catalyst_uniform_bound`

 The catalyst is bounded by a natural number independent of the power. 
