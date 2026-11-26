---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerPersistence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerPersistence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerPersistence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Persistent traversal parameters during the role and row scans

Only six terminal scalars are used by the traversal workers. Their level
scalars all precede the row arena. Agreement on these words therefore
preserves each chronological worker's count, role and parameter bank.


### `terminalScalars`

 The terminal words read by the traversal stage. 

### `Resident.transfer`

 Transfer resident scalars after any partial scan. Only the terminal
words read by the controller need survive writes in the high header. 

### `selected_prefix_schedule`

 Every reference prefix sees the same selected schedule and initial
site count when its row and tag writes preserve the resident headers. 
