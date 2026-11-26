---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Reservations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Reservations.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Reservations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Summing the charges for propagated splits

The propagation weight doubles every eight levels. Splits at depth `j`
below a base are paid for at rate `min (2^-k) (2^-j)`, where the minimum
base length is `F = 2^k`. The sum is at most `24 * 2^⌈k/8⌉ / 2^k`.


### `small_resetWeight`

 The required minimum base length depends only on the safety margin
and error tolerance, even with arbitrarily many tether neighbors. 


# Excess loads in the degree reset

Normalize by the capacity `FB`. Loads at most `1/F` with base mean
at most one obey two complementary bounds. The variance pays for near
overloads and the off-diagonal term for distant ones.


### `estimate`

 Only quadratic moments in this estimator depend on the permutation. 

### `weighted_estimate`

 A bound for a single position, to be summed over positions and contacts. 

### `spills`

 A contact reserves its mean plus a fixed safety margin. 


# Reservations between pairs of bases

Two dyadic cells that intersect are nested. Thus each contact is indexed
by a cell at the finer of the two depths, with endpoints obtained by
taking prefixes. Its capacity is the mean over all such cells plus a
safety margin independent of the mixer.


### `reservation_bound`

 The reserved capacities at a base cost at most two normalized units. 


# Mixing block indices by a field multiplier

Identify binary block indices with a field of order `2 ^ h`. As the
multiplier ranges over units, the difference of any two distinct indices
visits each nonzero vector once. At most `2 ^ (h-i) - 1` of these vectors
have zero prefix of length `i`.


### `mixer`

 A single family of linear permutations works simultaneously at all depths. 

 # Common reservations and term-specific layers for the core reset 

### `Port`

 A reserved link has one slot at each end with the same index. 

### `Delivery`

 Attach whole input occurrences to terminals. At both ends of each good
unit, select a distinct port on a layer connecting to the reserved link. 

 # Programming a tagged verifier by fixing the output tags 

### `tag_program`

 Designate fixed, distinct input and output positions for the rotor.
Only the positional tags are programmed by the permutation. 
