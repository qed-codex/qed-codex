---
{
  "module": "OAI/Algorithms/SubexponentialSAT/FourWordPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FourWordPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FourWordPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Four runtime-width words in flat and bank representations

Eight distinct caller ports hold a flat record, unary field width, counter,
temporary stack, and four bank words. The number four is fixed in the control;
the field width is exclusively stack data.


### `splitCmd`

 Ports 0/1/2/3 are flat input, width, counter, and temporary; ports 4–7
receive the four words in their original bit order. 

### `packCmd`

 Copy the words in reverse call order so their flat output order is 0,1,2,3.
The word bank is preserved. No width is needed for packing. 
