---
{
  "module": "OAI/Computability/VPVNP/PairNativeCachePaper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCachePaper.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCachePaper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The native cache initializes the prescribed auxiliary leaf sources 

### `paper_run`

 Cache preparation in the paper's actual eleven-operand row, using only
the runtime cache-base register, the fixed exponents, and the parsed prefix.
Each of the 38 private cells is exactly the scalar the virtual leaf reads. 
