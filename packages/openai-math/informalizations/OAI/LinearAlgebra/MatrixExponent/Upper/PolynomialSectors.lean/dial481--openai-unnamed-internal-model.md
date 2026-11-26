---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialSectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialSectors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/PolynomialSectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The three-sector polynomial degeneration

These are the coefficient identities of Section 5.2.  The first input has
weight zero throughout the degeneration.  Only when identifying the individual
middle branch do we reverse its first index; its other two indices are swapped.


### `triplingWidth`

 The second input length in the tripling construction. 

### `triplingYWeight`

 The middle interval of the second input has weight one. 

### `triplingZWeight`

 The middle output-dual interval has weight minus one. 

### `triplingMatched`

 The three matched pairs of intervals, expressed with exclusive upper bounds. 

### `tripling_support_middle`

 A supported middle output can only come from the middle second input. 

### `tripling_weight_nonneg`

 No nonzero convolution coefficient has a negative total weight. 

### `tripling_weight_zero_iff`

 Precisely the three matched sectors survive in weight zero. 

### `tripling_weight_one_iff`

 Every term that disappears has weight exactly one, and goes from the
middle second-input sector to one of the two outer output sectors. 

### `triplingGraded`

 The simultaneous weight-zero tensor, with one unchanged shared first leg. 

### `triplingGraded_coefficient`

 The full coefficient formula includes all vanishing cross-sector terms. 

### `triplingLeftY`

 Translate a coordinate into the left second-input sector. 

### `triplingLeftZ`

 Translate a coordinate into the left output sector. 

### `triplingMiddleY`

 Translate a coordinate into the middle second-input sector. 

### `triplingMiddleZ`

 Translate a coordinate into the middle output sector. 

### `triplingRightY`

 Translate a coordinate into the right second-input sector. 

### `triplingRightZ`

 Translate a coordinate into the right output sector. 

### `triplingReverse`

 Reversal used only in the middle branch identification. 

### `tripling_left_coefficient`

 The left branch is exactly polynomial multiplication of lengths `a,h`. 

### `tripling_right_coefficient`

 The right branch is the same tensor after translations on the last two legs. 

### `tripling_middle_coefficient`

 In the middle branch the second and third tensor legs are exchanged, and
the first basis is reversed.  This identity does not reverse the first basis
of either outer branch or of the whole simultaneous degeneration. 

### `tripling_second_sectors_disjoint`

 The three second-input images are pairwise disjoint. 

### `tripling_output_sectors_disjoint`

 The three output images are pairwise disjoint as well. 

### `TriplingY`

 The three complete second-input sectors, before forgetting their labels. 

### `TriplingZ`

 The corresponding complete output sectors. 

### `triplingYMap_surjective`

 All second-input coordinates occur in exactly one sector. 

### `triplingZMap_surjective`

 All output coordinates occur in exactly one corresponding sector. 

### `triplingYEquiv`

 A single simultaneous second-input basis equivalence. 

### `triplingZEquiv`

 A single simultaneous output basis equivalence. 

### `triplingSectorTensor`

 The actual common-first-input assembly.  Its middle summand, in the same
first-input coordinates as the outer summands, has reversed first coefficients.
Every cross-sector coefficient is zero. 

### `triplingGraded_sector_assembly`

 Reindexing the last two legs by their single complete sector equivalences
gives the full assembled tensor.  The first input is literally unchanged. 
