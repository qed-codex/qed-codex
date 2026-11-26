---
{
  "module": "OAI/Computability/VPVNP/ExtensionAmplification.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExtensionAmplification.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExtensionAmplification.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite amplification for exact spectral extension

In Theorem 2.4 of *VP and VNP differ over every field*, a uniform multiplicative
discrepancy on a finite list of generators is amplified by doubling or removing
one exponent of a balanced product. Positive integer coefficients make the
resulting variants dominate the balanced product at every competing spectral
point, while their total target value is less than half its scaled target.


### `amplificationExponent`

 Either double or remove one exponent of the balanced product. 

### `amplificationWeights`

 Integer amplification multiplicities with a common scale for finitely many positive weights. 

### `finiteProfileAmplification`

 A single balanced monomial and positive integer multiples of its variants
separate the target profile from every profile with a uniform multiplicative gap. 
