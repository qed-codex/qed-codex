---
{
  "module": "OAI/Computability/VPVNP/GrassmannTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannTypes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The binary Grassmannian and its distance classes

Section 5.1 uses the action of linear automorphisms on the ordered pairs of
middle-dimensional subspaces of a binary vector space. The type of a pair
is its sum dimension minus the common dimension of the subspaces.


### `Space`

 The ambient binary vector space of dimension twice the plane dimension. 

### `Plane`

 Middle-dimensional subspaces of the ambient space. 

### `HasType`

 The paper's type of an ordered pair, determined by its sum dimension. 

### `Pair`

 All ordered pairs of type `r`. 

### `GL`

 Linear automorphisms of the ambient binary space. 

### `IsSquare`

 The four side types and two diagonal types of a Grassmann quadrilateral. 

### `mean`

 The uniform mean of an array over all ordered pairs of type `r`. 
