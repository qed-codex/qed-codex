---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Space preservation by the two-tape stack compiler

At every instruction boundary, the first head has moved left by the growth
in the packed bank since initialization, and the scratch head has returned
to its initial cell. An unfinished instruction can move either head by at
most its own linear scan time. These bounds do not accumulate with the
number of completed instructions.


### `Reach`

 Stack states on any branch starting from the specified initial bank. 

### `HeadBox`

 Each tape head lies in the interval from minus the radius to plus the radius. 

### `headPath_space`

 On either tape every cell visited by every finite prefix lies within
radius 7M+4 of the initial head, uniformly over the execution time. 
