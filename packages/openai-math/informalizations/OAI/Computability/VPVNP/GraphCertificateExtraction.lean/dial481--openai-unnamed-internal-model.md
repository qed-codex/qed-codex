---
{
  "module": "OAI/Computability/VPVNP/GraphCertificateExtraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphCertificateExtraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphCertificateExtraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Bounded certificates from a monic graph relation

Replace the normalized graph coordinates by their linear parts. The difference
between the two substitutions is an explicit combination of the equations.
Its multipliers grow in degree by at most the maximum substitution degree for
each variable in a monomial. Taking the leading power of the graph parameter
then produces a certificate for one.


### `specialize_parameter`

 Replacing the normalized coordinates by polynomials independent of the
parameter amounts to mapping the coefficients of the univariate relation. 

### `graph_monic_certificate`

 Extract the bounded certificate for an inconsistent system from a monic
relation on a linear Noether normalization of its graph. 
