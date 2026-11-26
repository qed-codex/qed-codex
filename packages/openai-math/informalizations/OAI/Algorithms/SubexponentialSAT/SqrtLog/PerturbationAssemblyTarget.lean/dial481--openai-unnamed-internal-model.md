---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyTarget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyTarget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyTarget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Dynamic target-jet cache installation. Full source-degree metadata at210
is untouched while the arithmetic count is temporarily changed to213. 

### `finishTarget`

 Restore all three original caches and release the point and scalar zero. 

### `target_restore_dictionary`

 The dictionary may change while the temporary caches are live. Restoring
those caches preserves precisely that completed dictionary. 
