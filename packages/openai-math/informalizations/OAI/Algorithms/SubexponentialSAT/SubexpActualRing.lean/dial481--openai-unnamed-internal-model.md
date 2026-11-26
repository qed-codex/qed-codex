---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpActualRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpActualRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpActualRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The counting ring from the executable quartic search

Both the residue field and the prime-power ring use the coefficients returned
by QuarticSearch. No separately chosen minimum polynomial enters this file.
The polynomial quotient is the semantic interpretation of those coefficients;
the executable four-coordinate arithmetic is implemented separately.


### `coordinatesOfDegree`

 Reindex the linear remainder coordinates by a proved exact degree. 

### `residuePolynomial`

 The polynomial selected by the executable exhaustive quartic search. 

### `F`

 Coefficientwise integer-representative lift of that exact polynomial. 

### `E`

 The actual residue field, defined by the selected polynomial. 

### `Ring`

 The actual prime-power ring, definitionally the quotient used by the
four-coordinate arithmetic refinement. 

### `F_map`

 Reduction yields the same selected residue polynomial. 

### `reducedEquiv`

 Transport along polynomial equality, with no choice of a new field. 

### `rho`

 The exact residue map used by the counting argument. 

### `coordinateLift`

 The standard integer representatives of prime-field coordinates. 

### `fieldCoordinates`

 Four residue-field coordinates in the power basis. 

### `nodeEquiv`

 A semantic enumeration of all nonzero field elements. Its implementation
on explicit coefficient words is a separate refinement obligation. 

### `ringCoordinates`

 The semantic ring is precisely a free module of four base-ring
coefficients; the coefficient-selection algorithm determines its modulus. 

### `sectionValue`

 The explicit residue section lifts the four standard coefficient
representatives individually. It uses no choice of preimages. 

### `sectionValue_algebraMap`

 On prime-field constants the section is exactly the original integer lift. 

### `residueSection`

 Package the explicit four-coefficient section for the beta interface. 

### `decodeCount`

 Decode the constant coefficient of the canonical remainder. 

### `decodeCount_eq_coordinate`

 Decoding reads precisely the first field of the four-coordinate representation. 
