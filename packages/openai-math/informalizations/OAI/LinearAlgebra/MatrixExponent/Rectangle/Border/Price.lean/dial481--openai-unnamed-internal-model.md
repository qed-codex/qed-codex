---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Price.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Price.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Price.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Specialization by a valuation

If every polynomial identity of a tuple holds at another tuple, one
valuation subring contains the first tuple and specializes it to the
second. The coefficients are fixed under specialization.



# A simultaneous spectral maximizer

Testing the weighted tensor tensored with many ordinary copies
finds a point attaining the ordinary maximum while retaining
the weighted lower bound. Only two observables of the compact
spectrum are needed.


### `detector`

 Exact lower bounds at all powers are detected by a single spectral point. 


# Generic rank decompositions

Over an infinite field the identities of rank-bounded tensors are
exactly the polynomial identities of the generic decomposition.


### `identity_of_rank`

 Base-field equations of a rank locus apply also to extension-field witnesses. 

### `integral_model`

 Only the tensor entries have to be integral at the place.
The summands of the generic decomposition may have poles. 


# One pivot for a border-rank decomposition

Choose a live output of maximal valuation in the first summand. Its
multiples cancel that summand on every live output, with the multipliers
integral at the chosen place. All other outputs are projected to zero.


### `shear_identity`

 A residue-field pivot works simultaneously for every diagonal rescaling
over the ground field and every polynomial identity of rank at most `r`. 


# Isolating an output cell

Independent scalings of rows and columns preserve the weighted product.
Scale every row and column other than the pivot's by a parameter. On the
sheared tensor this gives a polynomial path whose value at zero simply
erases the pivot. Polynomial identities persist at zero.


### `erase`

 Erase one cell of a nonempty set, dropping the border rank budget by one. 

 # Coordinate deletion in geometric border rank 

### `BorderRankLE.delete`

 Retaining some set of exactly `q` output cells lowers the geometric
border-rank budget by the number deleted. No hypothesis on the field or
on the rank of the retained set is required. 


# Spectral sublevels are Zariski closed

The rank interpolation argument works for any spectral point because
a linear combination costs at most the sum of its constituent prices.


 # Weighted products as three-site spectral tensors 

### `tensor_full`

 Tensor products retain a full-support weighting after pairing the
indices on each side. 


# Powers and field transfer for geometric border rank

Powering is a polynomial map of coefficient spaces, so exact
decompositions suffice to verify its action on the closure.


### `BorderRankLE.small`

 Adjoin the weights together with countably many distinct elements
of the algebraic closure. Infinitude ensures rank-locus identities
over this smaller field apply over the entire closure. 
