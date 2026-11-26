---
{
  "module": "OAI/Computability/VPVNP/EffectiveNullstellensatz.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EffectiveNullstellensatz.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EffectiveNullstellensatz.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The effective weak Nullstellensatz bound for the evaluator

Section 8.2 uses the multiplier bound `(2D)^(4(n+2))` over algebraically
closed fields. We prove it using the graph of the equation values, a linear
Noether normalization, and a bounded Perron relation. Integral closedness
makes the minimal relation monic, and taking its top parameter coefficient
gives a bounded certificate. This also supplies the effective hypothesis
in the Macaulay row test of Appendix D.1.


### `effective_weakCertificateBound`

 Every inconsistent degree-`D` system in `n` variables has a certificate of the
explicit degree used in the paper. The equation count and the characteristic are arbitrary. 

### `row_test_effective`

 The actual effective bound in the evaluator's row-space test for radical membership.
The tested polynomial and the matrix may be defined over a smaller base field. 
