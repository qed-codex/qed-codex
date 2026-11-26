---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Crossing/Form.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Crossing/Form.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Crossing/Form.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Splitting a binary form between its two affine charts 

### `split`

 Evaluate at the common diagonal by taking complementary initial jets. 


# A polynomial four-site sphere

Place the four marks at zero, X², Y² and infinity. Remove the poles
at zero by scaling every incident generator by its doubled energy.
At X² = Y² share the pole between the two middle marks asymmetrically,
charging mode m by m+1 on one side and by m on the other. On blocks
of equal length these two corrections to total degree cancel.


 # Degree of the four-site crossing form 


# The diagonal specialization

At the collision the second corner can pair only with the third. Equal
lengths force those two corners to pair fully with each other, leaving
the ordinary Kronecker pairing of the two remaining wedges.


### `CrossingSlice`

 A four-site pairing split at fixed levels. The middle two ordered
wedges have the same length. 

### `FiniteCrossing`

 Finite-energy bounds on the two alternative factorizations. 


# Crossing independent wires

At the second corner use the fusion preimage of each matrix unit with
vacuum output. Record the energy and length of the preimage on each cut.
The length filter makes unequal-length input pairs vanish.



# Shifted crossings from finite energies

Take the input levels just under two quadratic energy budgets. Shrinking
the output budgets slightly leaves room for the polynomial factors in the
finite crossing and for the loss in level selection.



# The two local charts of the crossing

At zero, fuse the first two finite sites. Interchanging the middle
blocks gives the expansion at infinity. In either chart the cleared
pole contributes one common polynomial factor at fixed energies.


### `local_chart`

 In a nilpotent chart the four-site form factors through one mode
space. The shared pole factor depends only on the incident energies. 

 # Factoring the low-degree coefficients in either chart 


# Shifted crossing by splitting a binary form

At equal coordinates the four-site polynomial is a product of two
pairings. The first coefficients factor across one cut. Read the
remaining coefficients backwards in the other chart for the other
cut. Fusion with vacuum output converts the middle pairing to a wire.

