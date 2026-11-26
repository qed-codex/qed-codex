---
{
  "module": "OAI/Computability/VPVNP/VacuumPairing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VacuumPairing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VacuumPairing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vacuum pairing in the shifted crossing

The empty-output matrix entry of the finite fermion field is the signed
Pascal minor in Appendix B. Coordinates of exterior products give the
determinant, and the energy-sector enumeration gives the same pairing as the
unimodularity calculation.


### `wedge_coefficient_det`

 The coordinate of a wedge on an ordered set of modes is a determinant. 

### `wedge_coefficient_eq_zero_of_card_ne`

 A homogeneous wedge has no coordinate in another occupation degree. 

### `rightProjection_kernel_single_one`

 At the empty output only deletion modes contribute, in increasing source order. 

### `vacuum_matrix_det`

 The vacuum matrix entry on an equal-cardinality sector is the signed
minor of the divided-derivative contraction matrix in Appendix B. 

### `vacuum_matrix_eq_zero_of_card_ne`

 Unequal occupation sectors have zero vacuum pairing. 

### `det_negativeCoefficient`

 The negative mode gives a sign depending on each row alone. 

### `signed_det_negativeCoefficient_eq_sectorPairing`

 With the order reversal from the vacuum contraction, the signed matrix is
exactly the integral pairing in each energy sector of Appendix B. 

### `sectorIndex`

 The same occupied modes in the larger mode cutoff used for the Wick identity. 

### `sectorIndex_order`

 Embedding into a larger cutoff preserves the increasing enumeration of the modes. 

### `vacuum_matrix_sectorPairing`

 The vacuum coefficient in the finite operator identity is the paper's
integral pairing, with identical orderings of the rows and columns. 

### `vacuum_matrix_crossingPairing`

 The simultaneous matrix of vacuum entries on all nonempty states of bounded
energy is the integral block matrix from Appendix B. 
