---
{
  "module": "OAI/Computability/VPVNP/GrassmannSampling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannSampling.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannSampling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Conditional sampling on adjacent Grassmannian planes

Section 5.2 of *VP and VNP differ over every field* samples a linear map
on the whole ambient space. On adjacent planes, the joint law of its basis
readings consists of one shared tuple on the intersection and two independent
values on the extension columns. Changes of basis express both endpoints in
the fixed vertex coordinates.


### `exists_adjacent_charts`

 For any observable of the two endpoints, the mean over all linear maps is
exactly the mean over the two extensions of the common restriction. Both
endpoint charts are independent of the observable. 
