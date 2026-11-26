---
{
  "module": "OAI/Computability/VPVNP/GrassmannGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# CAT(0) quadrilaterals

The proof of Lemma 5.3 of *VP and VNP differ over every field* averages
the squared quadrilateral inequality over subspace rectangles. At equality
both pairs of opposite sides have equal lengths.


### `quadrilateral_sq`

 The squared quadrilateral inequality (4.3), with cyclic vertices `a,b,c,d`. 

### `quadrilateral_eq_opposite`

 Equality of the squared diagonals and sides forces equality of opposite
side lengths, as used in the Grassmannian rigidity argument. 
