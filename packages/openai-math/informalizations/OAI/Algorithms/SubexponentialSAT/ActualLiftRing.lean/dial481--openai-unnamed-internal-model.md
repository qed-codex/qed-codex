---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ActualLiftRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ActualLiftRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ActualLiftRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The actual prime-power counting ring

The defining polynomial is the minimum polynomial already constructed for
`FiniteField.E p h`. A monic lift gives Lambda. Reduction followed by the
proved quotient equivalence lands in that exact field, not merely some field
of the same cardinality. The only numerical side conditions are positivity
of the modulus exponent and, for degree-dependent decoding, `h ≠ 0`.


### `chosenF`

 Choose a monic lift when the modulus exponent is positive. The zero case
only keeps the type of the ring free of proof arguments and is never used by
counting. 

### `Ring`

 Lambda = (Z/p^mu Z)[Y]/(chosen monic lift). 

### `reducedEquiv`

 Transport the reduced polynomial quotient to the exact interpolation field. 

### `rho`

 The actual residue map used in symbolic counting. 

### `coordinateLift`

 Lift prime-field coordinates using their standard integer representatives. 

### `residueSection`

 A residue section; no ring-homomorphism property is required or claimed. 

### `decodeCount`

 Recover the integer represented by a constant element, using remainder
coordinates in the actual chosen polynomial quotient. 

### `liftedLayout`

 All rows and nodes of an actual layout lift to the chosen counting ring. 
