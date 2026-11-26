---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgmin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgmin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgmin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A binary-score minimum update implemented by finite bit programs

The score is a little-endian bit word. Comparisons inspect its numeric value,
not its length. Candidate payloads may themselves be binary indices or encoded
rows. Ports 0/1 hold the incoming payload/score, 2/3 the incumbent, 4--7 are
scratch, and 8 is an untouched caller queue. Every copy and comparison below
has a measured trace of a fixed finite instruction table.


### `compare_eval`

 Destructive binary comparison; only scratch stacks 4, 5, 6 change. 

### `update_eval`

 One strict-improvement update. The bound depends on bit lengths, never on
the numeric score. The queue and the first incumbent on equal scores survive. 
