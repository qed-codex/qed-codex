---
{
  "module": "OAI/Computability/VPVNP/HardnessDegrees.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessDegrees.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessDegrees.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Assembling the homogeneous parse layers

The graded grammar of §8.1 represents the positive-degree pieces of a circuit.
Its scalar output at degree zero must also be retained when expanding a general
VNP witness summand. The number of grammar states uses the variables and the
binary gates of the exact circuit.


### `eq_constant_add_positive_components`

 The constant term plus all positive homogeneous components recover the formal polynomial. 

### `grammarFor`

 Choose a single table of labels from an exact circuit of minimum size. 

### `leafValue`

 Under witness specialization, a leaf either contributes a visible variable or
the field constant zero or one selected by the witness bit. 

### `witnessValue_eq_constant_add_parses`

 The exact specialization at any witness, as a sum of scalar-weighted ordered parses. 

### `grammar_bounds_of_isVP`

 A VP summand supplies polynomial bounds on both the number of positive layers
and the number of states, even when the intermediate circuit degrees are much larger. 
