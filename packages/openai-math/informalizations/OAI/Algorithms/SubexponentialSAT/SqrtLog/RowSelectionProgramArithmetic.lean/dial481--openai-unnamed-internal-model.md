---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionProgramArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact signed arithmetic for minor enumeration. Integers are represented as
pairs of natural binary words. No modular arithmetic, integer oracle, or
parameter-dependent instruction table is used. 

### `multiplyCommand`

 Inputs 0,1 represent the first integer and 2,3 the second. Outputs 6,9
represent their product. Ports 4,5,7,8 contain intermediate products; 10--14
are restored empty. All input words are preserved. 
