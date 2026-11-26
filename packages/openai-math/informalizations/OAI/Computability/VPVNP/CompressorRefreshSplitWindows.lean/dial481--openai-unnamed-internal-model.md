---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshSplitWindows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshSplitWindows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshSplitWindows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Three consecutive online windows around the refresh selector

Each native subwalk retains its reports while the dispatcher computes its
own rows. The earlier physical columns and the level header survive all
three subwalks, since every worker writes only to its refresh workspace.


### `selectWindow`

 The one-stage window for selecting a refresh term, immediately after the refresh
preparation stages. 

### `finishWindow`

 The window for the remaining refresh stages after the selected term. 

### `EntryState`

 The three incoming memory facts needed by all refresh subwindows. 

### `attach_part`

 Attach one contiguous subwalk and retain its exact report list and
the state of the header needed by the next subwalk. 
