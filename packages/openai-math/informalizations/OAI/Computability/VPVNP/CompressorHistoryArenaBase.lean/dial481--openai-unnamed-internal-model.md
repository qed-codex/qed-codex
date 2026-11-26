---
{
  "module": "OAI/Computability/VPVNP/CompressorHistoryArenaBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorHistoryArenaBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorHistoryArenaBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the initial history arena and traversal bounds

After the stride pass, the row count and level stride suffice to compute
the exclusive end of the tight descriptor allocation. The pair-ABI program
writes that end to scalar 14 of the first level, the level count to scalar
28, and the live input length to scalar 29. All source expressions run
before any of the three external stores.


### `table`

 One fixed pair-ABI table performs the three separated stores. 

### `report`

 Native report publishing the history arena base, allocated level count, and input length in
the first level header. 

### `cost`

 Instruction count for computing and publishing the three initial history fields. 

### `probes`

 Number of external probes for history setup, including the three header stores after
evaluating the recipe. 

### `install`

 The exact three memory updates produced by the stage. 

### `native`

 Exact native execution after the chronological count and level stride
have been published. All cells outside the three destinations are preserved. 

### `stored`

 The first-level scalars hold the full natural numbers for the history
traversal, including the exclusive end of the arena allocation. 
