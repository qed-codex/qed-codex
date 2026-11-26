---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendShadow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendShadow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendShadow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual frontend has a query-only polynomial step budget. Selected
stack growth therefore bounds every visible output and every prefix without
charging any suspended caller word. This uses the original execution directly;
no new query evaluator or replacement run is introduced. 

### `marked_time`

 The actual source-only budget applies to this exact occurrence of the
marked command by determinism, with arbitrary retained caller words. 

### `marked_resources`

 Exact endpoint contents and guard facts remain those of he. Only their
visible lengths are bounded, by per-stack growth on the same compiled trace. 

### `marked_front_resources`

 The exact physical FrontState and the visible lower-bank cap required by
NativeQueryPreparation.front_resources come from the same frontend Eval. 

### `accepted_resources`

 The unmarked final frontend satisfies the same pointwise resource rule. 

### `marked_denominator_empty`

 The real marked frontend preserves the spare denominator word required
by preparation; its entry emptiness follows from the actual clean workspace. 

### `accepted_denominator_empty`

 The history-only frontend leaves the same actual preparation scratch empty. 
