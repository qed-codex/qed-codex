---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical coordinates and binary encoding for the selected quartic quotient

The four-coordinate representation denotes the exact quotient by
`QuarticSearch.poly c`. Its inverse is mathematical canonical-remainder
extraction. Binary operations on already supplied coefficient words remain
the executable operations of `SubexpQuarticRing`; no runtime claim is made
for extracting coordinates from an abstract quotient value.


### `quadEquiv`

 A four-field record and a function on Fin 4 contain the same data. 

### `coordinatesOfDegree`

 Reindex the canonical quotient coordinates by a known degree. 

### `quarticCoordinates`

 Canonical coordinates of the actual monic quartic quotient. 

### `quotientEquiv`

 The record representation is equivalent to the exact polynomial quotient. 

### `quotientDenote_injective`

 No two different coefficient records denote the same quotient element. 

### `quotientDenote_surjective`

 Every quotient class is denoted by a four-coordinate record. 

### `quotientCoefficients`

 Mathematical canonical coefficient extraction from an abstract quotient. 

### `quotientCoefficients_toFn`

 The inverse record contains exactly the four coefficients of the unique
degree-below-four remainder polynomial. 

### `encodeQuad`

 Exactly four fixed-width base-coefficient words, in increasing degree order. 

### `encodeQuad_eq_stack`

 Relation to the already verified fixed-width block concatenation. 

### `primePower_one_lt`

 Positivity of the modulus exponent makes the prime-power base nontrivial. 

### `encodeQuotient`

 Canonical binary representation of a quotient by any supplied monic quartic.
Coordinate extraction is noncomputable here; executable record arithmetic is
provided separately by SubexpQuarticRing. 

### `encodeQuotient_quotientDenote`

 A concrete coefficient record is encoded directly by its four words;
passing through the quotient does not change its representation. 

### `SelectedRing`

 The selected ring is exactly the quartic whose coefficients the executable
search returned and then lifted; no alternate field presentation is selected. 
