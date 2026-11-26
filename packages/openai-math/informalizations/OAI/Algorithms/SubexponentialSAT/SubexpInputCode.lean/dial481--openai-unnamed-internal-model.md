---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpInputCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInputCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInputCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable residue-row dot products and beta inputs

The programs use explicit coefficient and input arrays indexed by Fin D.
The dot-product loop performs D multiplications and D additions. A lift is
supplied as an ordinary executable backend function; its implementation cost
is kept separate rather than silently counted as one scalar operation.


### `dotListWithCost`

 Traverse a supplied list, doing one multiplication and one addition at
each coordinate. The returned natural number counts those scalar operations. 

### `dotWithCost`

 Complete finite dot product; the coordinate enumerator is executable. 

### `dotInputReads`

 Two supplied array entries are read at each coordinate. 

### `beta`

 Compute the residue dot product and apply the supplied lift function.
No section is chosen by an existence theorem inside this definition. 

### `betaWithCost`

 Compose the explicit dot-product program with an instrumented scalar
backend lift. The backend's own returned cost remains visible. 

### `map_dotWithCost`

 Dot products commute with the supplied residue-ring homomorphism. 

### `reduce_eval_linearForm`

 Coefficientwise and input-coordinate lifts give exactly the expected
residue dot product. The hypotheses are concrete pointwise lift equalities. 

### `beta_eq_lift_reduced_eval`

 The computed beta is exactly the chosen lift of the lifted row's residue. 

### `beta_defect_residue_zero`

 The beta computed by the program has the required zero-residue defect. 

### `beta_defect_dvd`

 Any independently verified kernel-as-divisibility theorem now supplies
the local p-divisibility premise used by the symbolic counting backend. 
