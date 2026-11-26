---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLinked.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLinked.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLinked.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the terminal root gather in the vertex image

The gather occupies the image's root-fields segment. Its nine temporaries
belong to that segment's private register bank. The eleven saved registers
are shared with the bootstrap, and the other three slots refer to the first
three DFS registers. The final exit enters DFS row zero.


### `imagePC`

 Physical program counter of a gather label in the vertex image's root-fields segment,
obtained from the finite numbering of gather instructions. 

### `imageWork`

 Embedding of the nine gather temporaries into the host registers allocated to the
root-fields segment. 

### `imageRegs`

 Actual placement of the three register groups in the image. 

### `image_linked`

 Every instruction of the installed segment has the linked labels, live
registers and DFS continuation of the gather proof. 
