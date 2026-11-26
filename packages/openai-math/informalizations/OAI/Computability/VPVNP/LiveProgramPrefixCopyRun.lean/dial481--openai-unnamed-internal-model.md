---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPrefixCopyRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPrefixCopyRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPrefixCopyRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Linked copying of the midpoint's active evaluator input prefix 

### `copied_with_tag`

 Retagging both reference and destination preserves the complete prefix-copy specification. 

### `prefixCopyBase`

 Base word address of the prefix-copy operand frame, eight words past the advice frame base. 

### `prefixCopyRun`

 Exact framed prefix-copy calls, including a single accepting skip for an empty prefix. 
