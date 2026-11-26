---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpResidueInverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpResidueInverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpResidueInverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable inversion by finite-field powering and nilpotent correction

The algorithm uses only scalar additions and multiplications, with explicit
finite loops. It constructs the entire inverse-difference table needed by CRT.
Its counters are ring-operation counts, not an assertion of machine time.


### `geometricHornerWithCost`

 A shared Horner recurrence for the finite geometric sum. 

### `inverseWithCost`

 Power to `q-2`, then correct the nilpotent defect. Negation is implemented
as multiplication by the fixed constant `-1`, and is included in the count. 

### `differenceInverseWithCost`

 Diagonal table entries are zero. Off-diagonal subtraction costs one
multiplication by `-1` and one addition before inversion. 

### `inverseTableWithCost`

 Materialize all entries once, in a finite array of finite arrays. 

### `residue_fermat_inverse`

 A finite-field Fermat power is an inverse after reduction. 

### `fermat_defect_nilpotent`

 The principal-kernel condition converts the residue defect into a
nilpotent element of the original, possibly non-field ring. 

### `crtFromResiduesWithCost`

 Complete preprocessing and reconstruction from residue-distinct nodes.
The supplied data contain no inverse elements. 

### `crtFromResiduesWithCost_fullNodeCost`

 For all nonzero residue-field nodes and `μ = D+1`, the entire inverse
preparation is absorbed by a fixed polynomial in the displayed CRT sizes. 

### `powerRun`

 Shared powering over concrete coefficient routines. The counter is the
sum of counters returned by those routines, including the initial one. 

### `hornerRun`

 The value representing one is cached by the caller. 

### `inverseRun`

 Concrete coefficient inversion using the shared represented-ring API. 

### `inverseTableProgram`

 The inverse table executed without carrying any semantic decoder. 
