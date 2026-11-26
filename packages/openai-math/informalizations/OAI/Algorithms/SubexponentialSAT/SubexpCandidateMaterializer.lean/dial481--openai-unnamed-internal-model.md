---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCandidateMaterializer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateMaterializer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateMaterializer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual candidate-to-assignment materialization steps

A candidate label is a little-endian bit word. The runtime unary chunk width
selects its low bits, and a finite scan checks that every higher bit is zero.
The low bits are written into the selected chunk of a packed Boolean array by
the existing finite array-update program. No semantic label test or array
update is an executable instruction.


### `store`

 Array, replacement, unary index, unary width, four scratch stacks,
unprocessed label, and the output validity bit. 

### `command`

 Fixed finite code, independent of the chunk index, label width, and array size. 
