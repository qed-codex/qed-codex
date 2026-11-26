---
{
  "module": "OAI/Computability/VPVNP/JointScalarResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resources of the joint signed scalar checker

The two shared subcircuits process grammar and clock witnesses. The final
layer compares row, exponent and motif words and forces unused banks to zero.
Gate count and all stack budgets are uniform in the query's numerical values.


### `finishBound`

 Size bound for the final Boolean expression that selects the equation and sign, compares
exponents and checks unused witness bits. 

### `frame_size_le`

 Combining subcircuits preserves sharing before the final layer is added. 

### `gateBound`

 The number of query-independent Boolean gates in the joint checker. 

### `adviceBound`

 Upper bound for the encoded Boolean checker length in terms of its gate count and query and
witness widths. 

### `choiceBound`

 Stack-step bound for testing one witness and advancing the enumerator for a signed
coefficient query. 

### `stackBound`

 Bound on the number of bits in each stack during the complete enumeration of coefficient
witnesses. 

### `specialized_le`

 Instantiate the bounds with the grammar incidence circuit and the actual
clocked path verifier at the given length. Both coordinate placements may vary
with the length. The threshold and all query bits are runtime inputs. 

### `gateBound_polynomial`

 All parameters except the grammar, its coordinate count, and its exponent
width are fixed independently of the input length. 

### `stack_bounds_polynomial`

 Convert gate count and physical word-bank lengths to bounds for the
actual unary-address advice program and the stack enumerator. 

### `specialized_polynomial`

 Polynomial resource bounds for the joint system in the formal coordinate
order, for every exponent width polynomial in the input length. The table
parameters depend only on the fixed motif system. 

### `checker_polynomial_resources`

 The same four polynomial bounds work for every physical query to the
fixed motif and grammar checker at every length `n ≥ 2`. The fourth bounds
the exponent of the exhaustive counting time. 
