---
{
  "module": "OAI/Computability/VPVNP/MacaulayQueryBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayQueryBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayQueryBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Widths of the numerical Macaulay queries

The binary logarithms of the certificate degree, powering exponent, raw
graded keys, and augmented matrix dimensions are bounded using the input
parameters of Lemma 8.2. The fixed radix-scan program uses a common register
width that also covers its digit sum.


### `scanWidth`

 An explicit common binary word width for every dense ordinal and for
the counting mode. The extra bit accommodates equality with the upper limit. 

### `bounded_query_dimensions`

 Row and column dimensions, and the word widths of each monomial lookup,
are polynomial on a binary logarithmic scale for the exact QueryData parameters. 
