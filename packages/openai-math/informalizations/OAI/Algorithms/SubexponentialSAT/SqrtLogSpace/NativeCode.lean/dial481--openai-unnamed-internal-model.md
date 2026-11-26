---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed physical stages for the streamed local-code and graph-code searches.
The retained search state is confined to the lower48 leaf stacks; selected
matrices are saved outside that bank before its paid cleanup. 

### `lowerPorts`

 The fixed lower-bank ports, kept opaque to prevent routine theorem
checking from reducing the complete cleanup program. 

### `searches`

 Graph first, followed by the local code. The two matrices are retained in
physical815/816 while the same lower workspace is reused. 

### `searches_eval`

 Both searched matrices are physically retained for serialization. The
second search starts from the polynomial matrix boundary, independently of
how many losing candidates the first search visited. 

### `searchBoundary_physical`

 Runtime unary dimensions already occupy physical input words. Thus the
retained matrices add only a fixed linear factor to the original word cap. 
