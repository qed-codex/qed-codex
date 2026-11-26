---
{
  "module": "OAI/Computability/VPVNP/GrassmannSeeds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannSeeds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannSeeds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinate configurations in the binary Grassmannian

Pair the coordinates in the ambient space and choose one from each pair. The
sum dimension of two resulting planes is the common plane dimension plus the
Hamming distance between the choices. Flipping two disjoint blocks of pairs
gives the quadrilateral used in the averaging argument of Lemma 5.3.


### `cubePlane`

 The coordinate plane spanned by row one in each marked pair and row zero
in every other pair. 

### `hasType_cubePlane`

 In the coordinate cube the Grassmann pair type counts exactly the pairs of
coordinates on which the two choices differ. 

### `exists_cube_face`

 The face on the first `ℓ` coordinate pairs. For `ℓ < m` its pair types
are all strictly below `m`, as required in the equality argument of Lemma 5.3. 

### `exists_square`

 Seed quadrilaterals for the Grassmannian averaging argument. Their
opposite sides have types `r` and `s`, and both diagonals have type `r + s`. 

### `exists_pair`

 Every distance type up to the plane dimension occurs. 
