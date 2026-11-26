---
{
  "module": "OAI/Computability/VPVNP/PairTraversalLeafWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLeafWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLeafWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writing the source-free leaf headers

The initial layer has no children. Its fixed worker computes the header address
from the site cursor, base and descriptor stride. It writes the pointer and a
zero count directly. Padding and other external words keep their old contents.


### `program`

 Fixed native instruction program that writes the empty child row for one cursor leaf. 

### `directory`

 Encode the leaf layer's row base and per-site pitch as the worker's two directory words. 

### `native`

 From the reset entry, emit exactly the two leaf header writes. 

### `run_layer`

 A complete leaf pass from site zero on arbitrary initial external memory. 
