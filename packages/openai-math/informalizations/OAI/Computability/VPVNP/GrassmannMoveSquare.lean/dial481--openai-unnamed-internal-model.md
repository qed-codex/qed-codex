---
{
  "module": "OAI/Computability/VPVNP/GrassmannMoveSquare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannMoveSquare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannMoveSquare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The quadrilateral of a completion-column move

In the equality argument of Lemma 5.3, replace one column of the common
completion by a vector outside the entire frame. The two original planes
and the two new planes form a square of types `r` and one. The sums across
the move use both the old and the new column, so their dimensions can be
read off from the extended independent frame.


### `completion_move_square`

 The old left, old right, new right, and new left completed blocks have
dimension `m`. In this cyclic order they form an `(r, 1)` square. 
