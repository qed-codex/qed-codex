---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRadius.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRadius.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRadius.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One length-dependent window for all middle-cut inputs

The raw input length and reachable stack storage are polynomially bounded
independently of the particular accumulated exponents. A fixed power of the
input length thus provides the radius the live RAM computes. The exponent
is chosen before the later group-width and processor constants.


### `fits_mono`

 Enlarging a head-relative window retains all the data of a bounded state. 

### `exists_length_radius`

 A single exponent and threshold bound the relative tape radius for every
admissible middle input and stack bound at each length. 

### `card_labeled_of_le`

 Apply the literal tail count at the common, length-only radius.
Each input may use strictly less stack storage and fewer input bits. 
