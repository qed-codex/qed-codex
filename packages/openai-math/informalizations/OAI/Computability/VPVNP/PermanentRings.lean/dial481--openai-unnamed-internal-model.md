---
{
  "module": "OAI/Computability/VPVNP/PermanentRings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentRings.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentRings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Variable rings in the permanent reduction

Each row of a variable ring chooses its own column or the next column cyclically.
Covering all columns exactly once forces a common choice throughout each ring.


### `RingRow`

 One ring of length `m + 2` for each of the `k` variables. 

### `ringTarget`

 The false edge stays in the column of its row. The true edge advances cyclically. 

### `ringChoice_step`

 Two consecutive rows of a permutation must make the same choice. 

### `ringTarget_bijective_iff`

 The destinations permute all ring positions exactly when each variable chooses
one of its two orientations consistently. 

### `ringDegrees_eq_full_iff`

 The full column monomial selects precisely the consistent ring choices. 

### `ringChoicesEquiv`

 Reading the orientation at position zero identifies consistent choices with
Boolean assignments to the variables. 

### `sum_ring_choices`

 After imposing the full ring-column degree, the sum over row choices counts
each Boolean assignment once, with its original weight. 
