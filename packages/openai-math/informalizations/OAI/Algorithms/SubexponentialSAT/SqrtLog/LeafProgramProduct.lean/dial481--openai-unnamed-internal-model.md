---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramProduct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A native fold of computed sparse factors. The input records contain actual
serialized sparse dictionaries. Each iteration parses one dictionary, invokes
the checked sparse product table, and reclaims the temporary operand. This is
the multiplication stage shared by hash indicators and the marked clause. 

### `callback_eval`

 The product callback has no abstract operation premise: its arithmetic
execution is obtained directly from the concrete sparse product program. 
