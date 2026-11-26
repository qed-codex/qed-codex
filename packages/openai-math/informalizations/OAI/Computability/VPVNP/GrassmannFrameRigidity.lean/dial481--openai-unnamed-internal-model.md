---
{
  "module": "OAI/Computability/VPVNP/GrassmannFrameRigidity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrameRigidity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrameRigidity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Independence of the original columns and their completion

The equality case of Lemma 5.3 first makes an observable on two completed
block spans independent of the choice of completion. Moving an original column
then preserves the observable as well: a common completion containing the
difference of the two columns gives identical completed block spans.


### `completed_blocks_rigid`

 If replacing a completion column outside the total span preserves the
observable, its value is the same on all pairs of completed blocks of the
given sizes. This holds over every field, including the binary one. 
