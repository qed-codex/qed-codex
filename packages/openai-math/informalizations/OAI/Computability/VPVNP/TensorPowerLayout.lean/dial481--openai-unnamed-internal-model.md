---
{
  "module": "OAI/Computability/VPVNP/TensorPowerLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The tensor-power layout bound for the universal family

The finite-state tensor-power verifier uses source length at most a constant times
`((2^b)^12)^h`. Thus the comparison with an `n^C` circuit uses the exponent `12*C`.
The constant may depend on the number of parties and the fixed digit width, while the
exponent twelve is independent of both. The terminal tensor below uses cardinality
indices `Fin (2^b)`, as in the star-witness construction.


### `power_lt_of_scaled_logb`

 A layout whose scaled length lies below the normalized logarithm of the witness
has strictly smaller spectral growth. 

### `value_reindex_terminal_array`

 A local reindexing of all terminal legs leaves their placed tensor's value unchanged. 

### `TensorPowerCNF.coeff_form`

 The `h`-fold tensor form from the machine construction records the ordered
product of the selected tensor entries. 

### `exists_digit_layout_witness`

 Reindex the star witness by binary digits and convert its normalized log
lower bound into a strict spectral growth comparison for every balanced cut. 

### `not_small_universal_of_tensorPower_layout`

 A star witness strictly above every balanced layout precludes infinitely many
small-circuit lengths. The exponent of the layout's central wire includes the length
overhead of the concrete literal projection. 
