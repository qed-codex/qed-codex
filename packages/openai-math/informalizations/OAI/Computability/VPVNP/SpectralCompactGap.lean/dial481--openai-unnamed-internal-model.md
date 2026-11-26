---
{
  "module": "OAI/Computability/VPVNP/SpectralCompactGap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCompactGap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralCompactGap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compactness margins for spectral comparison and exact extension

Appendix A.1 turns a pointwise strict comparison into a single integer
margin. In the proof of Theorem 2.4, failure to match every prescribed
generator yields a finite set of generators and a single multiplicative
margin, in one of the two ratio directions.


### `spectrumValues`

 Monotone semiring homomorphisms, viewed in the ambient space of
real-valued functions on the restriction semiring. 

### `spectrumValues_isCompact`

 Tychonoff compactness for the spectral points of Section 2. Each tensor
coordinate lies between zero and an integer rank bound. 

### `compact_strict_comparison_margin`

 A uniform integer margin for strict comparison over a compact spectrum,
with the topology of pointwise convergence. 

### `compact_finite_generator_gap`

 A finite set of generators detects every failure to match the target
values with a uniform relative gap. It can include any specified generators. 
