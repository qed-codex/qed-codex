---
{
  "module": "OAI/Computability/VPVNP/ParseHistogram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseHistogram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseHistogram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Production histograms for ordered grammar parses

In §§8.1 and 9.3 of *VP and VNP differ over every field*, each occurrence of a production
adds one to its label's exponent. The paired-word coefficient counts an ordered tree
together with a bijection from its leaves to the positions of the queried word.


### `histogram`

 The exponent of each terminal or binary production label in a given ordered parse. 

### `universalGrammar_weight_eq_histogram`

 Every occurrence contributes its own label, and multiplication adds the occurrences. 

### `histogram_degree`

 A parse with `d.val + 1` leaves uses `d.val` internal labels and one terminal label per leaf. 

### `ParseChoice`

 One of the choices counted in the coefficient query, retaining the ordered tree
and its bijective assignment to the paired bit positions. 

### `labelQuery_eq_sum_histogram`

 The query polynomial `Bₓ` is the integer sum of the histogram monomials of its parses. 
