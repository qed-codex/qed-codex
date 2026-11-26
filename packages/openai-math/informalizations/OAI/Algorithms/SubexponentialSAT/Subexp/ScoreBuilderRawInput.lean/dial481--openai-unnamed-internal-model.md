---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRawInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRawInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderRawInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Score-builder inputs from physically generated raw pair plans

The runtime pair table is retained in its actual generated order. A
permutation proof connects that order to the mathematical vertex-pair list;
the code never decodes plans back to vertex identifiers.


### `inputFor_of_memory`

 The two subroutine input conditions follow from the actual memory and high-stack invariants. 

### `scoreBytes_eq`

 Raw pair order changes neither candidate order nor the exact natural
score encoded by the physical candidate loop. 
