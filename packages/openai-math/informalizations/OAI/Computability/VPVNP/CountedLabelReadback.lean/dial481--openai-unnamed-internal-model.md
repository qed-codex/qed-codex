---
{
  "module": "OAI/Computability/VPVNP/CountedLabelReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CountedLabelReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CountedLabelReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two counted scalar queries of Section 8.1

The joint reader uses the same fixed counting machine with two choices of
Boolean circuit advice. One circuit counts the incidence words for a parse
histogram, and one counts the zero-padded witnesses of the universal machine.
A grammar exponent too large for the degree of the queried polynomial
returns zero before invoking the counter.


### `countBits`

 The binary output in the count stack of the fixed enumerator. 

### `pathScalar`

 The constant coefficient is read from the clocked path-count query. 

### `parseScalar`

 The production-counter callback uses `2n` bits per queried exponent.
Larger exponents cannot occur in a degree-`2n-1` parse monomial. 

### `countedCoeff`

 Integer coefficient lookup with both counted callbacks instantiated by
the outputs of the fixed circuit enumerator. 
