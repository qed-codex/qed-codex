---
{
  "module": "OAI/Computability/VPVNP/GrammarLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarLabels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer polynomials in the grammar labels

In §8.1 of *VP and VNP differ over every field*, the label equations (8.1) use
one indeterminate per terminal or ordered binary production. Here `labelQuery`
is the polynomial `Bₓ` read at a specified state. Every parse with `a` leaves
contributes exactly `2a - 1` label factors.


### `GrammarLabel`

 A terminal production is indexed by its state and variable. A binary production
records the parent layer and state, the split, and the two ordered child states. 

### `universalGrammar`

 The state table over the integer polynomial ring with distinct indeterminate labels. 

### `ParseGrammar.labelValue`

 The scalar assigned to each production label by a given grammar. 

### `ParseGrammar.specializeLabels`

 Specialize the universal integer labels to the entries of `G`. 

### `card_grammarLabel`

 Count all scalar labels, keeping the split index of each layer explicit. 

### `ParseGrammar.specialize_universalGrammar`

 Substituting the scalar labels commutes with evaluation at each state. 

### `ParseGrammar.specialize_coefficient`

 Specialization of every formal coefficient of the universal grammar. 

### `labelQuery`

 The integer coefficient query `Bₓ` of (8.1). At the start state the layer has
value `m - 1`, and the queried polynomial has degree `m` in the paired variables. 

### `universalGrammar_weight_isHomogeneous`

 Each tree uses one label per terminal leaf and one per binary internal vertex. 

### `universalGrammar_coeff_isHomogeneous`

 Reading any coefficient in the input variables leaves a homogeneous polynomial
in the production labels. 
