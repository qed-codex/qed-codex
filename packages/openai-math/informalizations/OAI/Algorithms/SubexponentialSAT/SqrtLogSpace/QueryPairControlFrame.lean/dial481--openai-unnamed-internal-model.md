---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairControlFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairControlFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairControlFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual emitted-pair callback excludes reads, peeks and writes on832/833.
The mask words834/835 remain real callback inputs. This certificate does not
cover the enclosing pair controller, which operates on its own traversal words. 

### `head_avoids`

 Every head-controller access is accounted for, including losing gates,
all binary counter tests and decrements, and final reclamation. 

### `accepted_avoids`

 The accepted path is instantiated with the actual source-table assignment
and dense addition/reset programs, with no callback footprint premise. 

### `tuple_controller_avoids`

 This covers the actual fixed attained-signature DFS, including all
presence tests, cursor scans and frame manipulation. 

### `visitor_avoids_of_loader`

 The fixed visitor composes the actual two passes and all arithmetic
without any access to the two suspended pair traversal words. 
