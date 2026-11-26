---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpAnnihilation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAnnihilation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAnnihilation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Simultaneous row annihilation for the multicolor layout

Section 3.3 of `source/subexponential-sat.txt`.  At a fixed interpolation
position, the same row annihilates every color different from its slot color.
The old two-color modules are preserved and used only for generic finite-sum
lemmas.


### `zeroExtendMatrix`

 Extend both row and column indices by zero. The membership tests are
explicit data, so this definition does not choose a representative. 

### `zeroExtendMatrix_map`

 Mapping coefficients commutes with the explicit zero extension. 

### `typeBlock_annihilation`

 Finite-sum cancellation at any color other than the slot color. The
selected matrix row is required to be supported on `Y`; no assertion is
needed about unrelated rows. Diagonal corrections are included. 

### `matrixPrescription`

 Explicit values for the single row path. The column's own head color
chooses which matrix supplies the value, as required by equation (3.8). 

### `matrixPrescription_on_side`

 At every active-side coordinate, the same prescription is the negative
row of that side's matrix; the zero extension handles both missing indices. 

### `rowForMatrices`

 The explicit multicolor polynomial row for a supplied matrix family. 

### `rowEvalForMatrices`

 Executable scalar evaluation of the same row formula, from the supplied
matrix entries, field operations, and explicit inverse data. 

### `rowCodeForMatrices`

 A finite expression tree for each polynomial row coordinate. Its
constructor is executable from the supplied matrix entries and inverse data. 

### `rowForMatrices_annihilates_of_fixed`

 The same interpolated row annihilates every other color, provided the
actual matrix family has the mismatch support asserted in equation (3.6). 

### `rowForMatrices_annihilates`

 Fixed-space form of the preceding theorem. The subspace is the canonical
multicolor subspace from the dimension module, not a second definition. 

### `universalRow`

 The single explicit polynomial row for the actual multicolor swap
matrices. The coefficients of the spectral polynomial are supplied directly. 

### `universalRow_annihilates`

 Section 3.3 for the actual swap matrix and explicit interpolation formula.
The mismatch support property is proved by the matrix construction, rather
than assumed. This one row annihilates every `g ≠ u.slot i t`. 
