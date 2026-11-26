---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderProtected.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProtected.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProtected.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native header machine preserves every address below its scratch base

The statement covers every successful native call, including calls started
on malformed input or intermediate memories. Thus the enclosing dispatcher
can keep its own stage tag immediately before the header scratch area.


### `component_protected`

 Each of the thirty-one source stages protects the lower part of memory
independently of the values read from scratch or processor words. 

### `native_protected`

 The linked header dispatcher itself preserves every word below the
scratch base. Its only extra write is to the inner tag at the base. 
