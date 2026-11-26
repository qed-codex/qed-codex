---
{
  "module": "OAI/Algorithms/SubexponentialSAT/LiftRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LiftRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LiftRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite free ring used for prime-power counting

This file constructs the quotient by a monic polynomial, proves that a
positive-degree quotient retains the base ring, and constructs coefficient
reduction maps between these polynomial quotient rings.


### `Extension`

 Quotient by the principal ideal of the defining polynomial. 

### `mk`

 The polynomial quotient map. 

### `of`

 The constant-polynomial map into the extension ring. 

### `base_injective`

 Constants embed for every monic defining polynomial of positive degree. 

### `remainder`

 The unique remainder is a linear function on the quotient. 

### `coordinates`

 Every residue class has one and only one vector of coefficients below
the degree of the monic defining polynomial. 

### `extension_finite_type`

 A finite coefficient ring yields a genuinely finite quotient ring. 

### `reduction`

 Change the coefficient ring in the quotient. 

### `reduction_eq_zero_iff`

 A principal kernel in the coefficient ring stays the same principal
kernel after adjoining a root of a monic polynomial. 

### `extensionField`

 Over a field, an irreducible defining polynomial makes the concrete
polynomial quotient a field. 

### `Base`

 The prime-power coefficient ring. 

### `Lambda`

 The ring Lambda in Section 4.1. 

### `baseReduction`

 Reduction of prime-power coefficients modulo p.  Primality is not
needed for this ring homomorphism. 

### `exists_monic_lift`

 A monic residue-field polynomial always has a monic lift of the same
degree; this discharges existence of the defining polynomial. 

### `residue`

 The residue-ring map induced by coefficientwise reduction. 

### `residueQuotientEquiv`

 Reducing Lambda modulo its ideal (p) is exactly the quotient by the
reduced defining polynomial, not merely a homomorphic image of it. 

### `label`

 Integer representatives of the prime-field labels. 

### `natCast_eq_zero_iff`

 Exact preservation of divisibility for constant natural-number counts. 

### `count_eq_zero_iff`

 A count strictly below the chosen modulus vanishes in Lambda exactly
when the ordinary integer count is zero. 

### `decodeCount`

 Read the constant coefficient as its standard nonnegative residue. 
