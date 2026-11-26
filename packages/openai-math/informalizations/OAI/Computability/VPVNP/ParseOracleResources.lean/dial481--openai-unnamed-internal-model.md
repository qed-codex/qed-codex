---
{
  "module": "OAI/Computability/VPVNP/ParseOracleResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resource bounds for the grammar coefficient checker

At length `n` the grammar of §8.1 has `n^(C+5)` states at each positive degree.
The bounds below are uniform over the root state and layer and over the placement
of grammar labels in the joint parameter list. The word and exponent values are
runtime inputs. They do not contribute to the advice length.


### `States`

 The `n^(C+5)` states available at each positive degree of the length-`n` parse grammar. 

### `flagCount`

 Number of independently enumerated event flags, including invalid events that
the fixed incidence clauses force to zero. 

### `rowBound`

 There is one tally row for each terminal variable and each grammar label. 

### `gateBound`

 Bound on the AND/NOT circuit gates for the queried exponent width. 

### `adviceBound`

 Length of the compiled gate stream, including its unary addresses. 

### `choiceBound`

 Uniform instruction budget for one choice of the event flags. 

### `stackBound`

 Bounds the height of every stack throughout enumeration. 

### `timeExponent`

 A polynomial exponent bounding the time to enumerate all flags. 

### `coefficient_query_runs_bounded`

 Run the actual checker on the joint query, with bounds independent of the
choice of layer, root state, address map, and queried values. 
