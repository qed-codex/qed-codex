---
{
  "module": "src/Lib/SiegelWeil/Tower/PrincipalIdeles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/PrincipalIdeles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/PrincipalIdeles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Principal ideles and a majorant on the complex torus

* `New.principalAdeleUnits`: the principal ideles, a discrete subgroup of the units of the adele
  ring.
* `New.integrable_prod_inv_one_add_log_sq`: `∏ x, (1 + (log |a x|) ^ 2)⁻¹` is integrable for Haar
  measure on `(ι → ℂ)ˣ`; it serves as a majorant at the infinite places.

Notions from other files:

* `New.CMType E`: E is a CM number field with, for each infinite place, a chosen complex embedding
  inducing it.
* `New.toAdele`: the diagonal embedding of E in its adeles, given at the infinite places by the
  chosen embeddings.
* `New.ratAdeles E`: the image of E under `New.toAdele`, a lattice in the adeles.


### `principalAdeleUnits`

 The principal ideles: the image of E^× in the unit group of the adeles. 

### `instance : DiscreteTopology (principalAdeleUnits E)`

 For a CM field E, the principal ideles, that is the image of E^× in the units of the adele ring,
form a discrete subgroup: they map into the discrete set `New.ratAdeles E`, the image of E in the
adeles. 

### `integrable_prod_inv_one_add_log_sq`

 For a finite index type `ι`, the function `a ↦ ∏ x, (1 + (log |a x|) ^ 2)⁻¹` on the group
`(ι → ℂ)ˣ` is integrable for Haar measure. 
