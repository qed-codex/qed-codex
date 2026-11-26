---
{
  "module": "src/Lib/Speed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Speed.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Speed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Speed settings

The three settings of this file make instance search and `simp` faster in all files of the
development. They add no axiom, and no proof relies on them: with this file emptied, the other files
still compile, more slowly.


### `New.IsVoid`

 A synonym of `IsEmpty` about which `simp` knows nothing. 

### `New.isEmpty_iff_isVoid`

 Many `simp` lemmas have a hypothesis `[IsEmpty α]`. When instance search does not find it,
`simp` tries to prove it. This lemma ends the attempt at once. 
