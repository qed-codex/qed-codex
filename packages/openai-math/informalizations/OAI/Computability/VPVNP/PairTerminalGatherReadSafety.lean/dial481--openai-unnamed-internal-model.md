---
{
  "module": "OAI/Computability/VPVNP/PairTerminalGatherReadSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalGatherReadSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalGatherReadSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # External read bounds of the terminal root gather

The inverse mate, width and prefix reads all use genuine arc ordinals. Each
bit read lies in its arc's interval in the shared array. When these arrays
end below the terminal header, every read belongs to the worker memory
that agrees between the source execution and its linked replay.


### `worker_readable`

 The three incidence arrays and the entire shared-bit interval suffice
to locate every individual read performed by the native root gather. 
